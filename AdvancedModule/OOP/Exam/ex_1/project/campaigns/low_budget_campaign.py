from project.campaigns.base_campaign import BaseCampaign


class LowBudgetCampaign(BaseCampaign):

    BUDGET = 2500.0
    INITIAL_RATE = 0.9

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, LowBudgetCampaign.BUDGET, required_engagement)

    def check_eligibility(self, engagement_rate: float):
        needed_engagement = self.required_engagement * self.INITIAL_RATE
        return True if engagement_rate >= needed_engagement else False
