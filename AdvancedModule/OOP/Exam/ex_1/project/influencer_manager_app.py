from typing import List

from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:

    VALID_TYPE_OF_INFLUENCERS = {
        'PremiumInfluencer': PremiumInfluencer,
        'StandardInfluencer': StandardInfluencer
    }

    VALID_TYPE_OF_CAMPAIGNS = {
        'HighBudgetCampaign': HighBudgetCampaign,
        'LowBudgetCampaign': LowBudgetCampaign
    }

    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in InfluencerManagerApp.VALID_TYPE_OF_INFLUENCERS:
            return f"{influencer_type} is not an allowed influencer type."

        current_influencer = self.find_influencer_by_name(username)
        if current_influencer:
            return f"{username} is already registered."

        new_influencer = InfluencerManagerApp.VALID_TYPE_OF_INFLUENCERS[influencer_type](username, followers, engagement_rate)
        self.influencers.append(new_influencer)

        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in InfluencerManagerApp.VALID_TYPE_OF_CAMPAIGNS:
            return f"{campaign_type} is not a valid campaign type."

        current_campaign = self.find_campaign_by_id(campaign_id)
        if current_campaign:
            return f"Campaign ID {campaign_id} has already been created."

        new_campaign = InfluencerManagerApp.VALID_TYPE_OF_CAMPAIGNS[campaign_type](campaign_id, brand, required_engagement)
        self.campaigns.append(new_campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        current_influencer = self.find_influencer_by_name(influencer_username)
        current_campaign = self.find_campaign_by_id(campaign_id)

        if not current_influencer:
            return f"Influencer '{influencer_username}' not found."

        if not current_campaign:
            return f"Campaign with ID {campaign_id} not found."

        if not current_campaign.check_eligibility(current_influencer.engagement_rate):
            return (f"Influencer '{influencer_username}' does not meet the eligibility criteria "
                    f"for the campaign with ID {campaign_id}.")

        payment = current_influencer.calculate_payment(current_campaign)
        if payment > 0.0:
            current_campaign.approved_influencers.append(current_influencer)
            current_campaign.budget -= payment
            current_influencer.campaigns_participated.append(current_campaign)

            return (f"Influencer '{influencer_username}' has successfully "
                    f"participated in the campaign with ID {campaign_id}.")

    def calculate_total_reached_followers(self):
        result = {}

        for campaign in self.campaigns:
            for influencer in self.influencers:
                for influencer_campaign in influencer.campaigns_participated:
                    if campaign.campaign_id == influencer_campaign.campaign_id:
                        if campaign not in result:
                            result[campaign]  = 0
                        result[campaign] += influencer.reached_followers(type(campaign).__name__)
        return result

    def influencer_campaign_report(self, username: str):
        influencer = self.find_influencer_by_name(username)

        return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        result = ["$$ Campaign Statistics $$"]
        sorted_campaigns = sorted([campaign for campaign in self.campaigns],
                                  key=lambda campaign: (len(campaign.approved_influencers), -campaign.budget))

        for campaign in sorted_campaigns:

            total_reached_followers = 0
            for influencer in campaign.approved_influencers:
                total_reached_followers += influencer.reached_followers(type(campaign).__name__)

            result.append(f'  * Brand: {campaign.brand}, '
                          f'Total influencers: {len(campaign.approved_influencers)}, '
                          f'Total budget: ${campaign.budget:.2f}, '
                          f'Total reached followers: {total_reached_followers}')

        return '\n'.join(result)

    def find_influencer_by_name(self, name):
        influencer = [i for i in self.influencers if i.username == name]
        return influencer[0] if influencer else None

    def find_campaign_by_id(self, campaign_id):
        campaign = [c for c in self.campaigns if c.campaign_id == campaign_id]
        return campaign[0] if campaign else None
