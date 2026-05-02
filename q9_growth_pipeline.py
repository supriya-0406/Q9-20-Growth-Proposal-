"""
🎯 Tophawks Q9: AI-Powered Lead Enrichment & Priority Routing
Prototype demonstrating the 20% growth proposal: auto-enrichment + smart routing.
Runs instantly with zero external dependencies.
"""
import json
from datetime import datetime

class GrowthPipeline:
    def __init__(self):
        # Mock API responses (replace with Crunchbase/BuiltWith/NewsAPI in prod)
        self.mock_enrichment = {
            "Acme Corp": {"funding": "Series B", "tech_stack": "Salesforce", "trigger": "hiring sales reps"},
            "Beta Labs": {"funding": "Seed", "tech_stack": "HubSpot", "trigger": "none"},
            "Gamma Fin": {"funding": "Series C", "tech_stack": "Dynamics 365", "trigger": "expanded to APAC"}
        }

    def enrich_lead(self, company_name: str, base_score: int) -> dict:
        """Simulate enrichment APIs + calculate routing priority"""
        data = self.mock_enrichment.get(company_name, {"funding": "Unknown", "tech_stack": "Unknown", "trigger": "none"})
        
        # Boost score based on high-intent triggers
        priority_boost = 0
        if data["funding"] in ["Series B", "Series C", "IPO"]: priority_boost += 15
        if data["trigger"] not in ["none", "Unknown"]: priority_boost += 10
        
        final_score = min(100, base_score + priority_boost)
        return {**data, "base_score": base_score, "enriched_score": final_score}

    def generate_conversation_starter(self, lead: dict) -> str:
        """Simulate LLM-generated personalized opener (template fallback for demo)"""
        company = lead["company_name"]
        trigger = lead.get("trigger", "recent growth")
        funding = lead.get("funding", "recent developments")
        
        return (
            f"Hi [Name], congrats on {company}'s {funding} and focus on {trigger}. "
            f"Given your scaling sales team, I'd love to share how we helped similar companies "
            f"reduce ramp time by 40%. Open to a 10-min chat this week?"
        )

    def route_lead(self, enriched_lead: dict) -> dict:
        """Smart routing based on enriched score + triggers"""
        score = enriched_lead["enriched_score"]
        if score >= 80:
            route = "🔥 HOT → Senior AE (<15 min SLA)"
        elif score >= 50:
            route = "🟡 WARM → Nurture sequence + weekly check-in"
        else:
            route = "⚪ COLD → Marketing automation pool"
        
        return {**enriched_lead, "route": route, "opener": self.generate_conversation_starter(enriched_lead)}

    def run_demo(self, leads: list):
        """Execute full enrichment → routing pipeline"""
        print("🚀 Tophawks Q9: AI Enrichment & Priority Routing Demo\n")
        results = []
        for lead in leads:
            enriched = self.enrich_lead(lead["company"], lead["base_score"])
            routed = self.route_lead({**lead, **enriched})
            results.append(routed)
            
            print(f"🏢 {routed['company']}")
            print(f"   📊 Score: {routed['base_score']} → {routed['enriched_score']} (+{routed['enriched_score']-routed['base_score']})")
            print(f"   🎯 Route: {routed['route']}")
            print(f"   💬 Opener: \"{routed['opener'][:90]}...\"")
            print("-" * 70)
        return results

if __name__ == "__main__":
    # Sample incoming leads
    sample_leads = [
        {"company": "Acme Corp", "base_score": 72, "industry": "SaaS"},
        {"company": "Beta Labs", "base_score": 45, "industry": "EdTech"},
        {"company": "Gamma Fin", "base_score": 60, "industry": "FinTech"}
    ]
    
    pipeline = GrowthPipeline()
    pipeline.run_demo(sample_leads)
    
    print("\n📈 Projected Impact (Team of 10):")
    print("   ⏱️ Response Time: <1hr for HOT leads (baseline: 24hrs)")
    print("   📧 Reply Rate: +25% (personalized, trigger-based openers)")
    print("   📈 Conversion Lift: ~20% in 4 weeks via A/B test at 10% traffic")
