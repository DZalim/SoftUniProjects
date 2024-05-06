from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class StandardInfluencer(BaseInfluencer):

    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)
        self.initial_payment = 0.45

    def calculate_payment(self, campaign: BaseCampaign):
        payment = campaign.budget * self.initial_payment
        return float(payment)

    def reached_followers(self, campaign_type: str):
        if campaign_type == 'HighBudgetCampaign':
            followers = self.followers * self.engagement_rate * 1.2

        elif campaign_type == 'LowBudgetCampaign':
            followers = self.followers * self.engagement_rate * 0.9

        return int(followers)
