from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):

    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)
        self.initial_payment = 0.85

    def calculate_payment(self, campaign: BaseCampaign):
        payment = campaign.budget * self.initial_payment
        return float(payment)

    def reached_followers(self, campaign_type: str):
        if campaign_type == 'HighBudgetCampaign':
            followers = self.followers * self.engagement_rate * 1.5

        elif campaign_type == 'LowBudgetCampaign':
            followers = self.followers * self.engagement_rate * 0.8

        return int(followers)
