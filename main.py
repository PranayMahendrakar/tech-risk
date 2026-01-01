#!/usr/bin/env python3
"""
Emergent Technology Risk Assessment Framework - Llama-Based Risk AI
Anticipates potential risks from new technologies and suggests mitigation strategies
Author: Pranay M
"""

import ollama
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, IntPrompt
from rich.markdown import Markdown
import json
from typing import List, Dict

console = Console()

TECH_DOMAINS = ["AI/ML", "Biotechnology", "Nanotechnology", "Quantum Computing",
                "Brain-Computer Interfaces", "Autonomous Systems", "Gene Editing",
                "Synthetic Biology", "Advanced Materials", "Space Technology"]

RISK_CATEGORIES = ["Safety", "Security", "Privacy", "Economic", "Social", 
                   "Environmental", "Existential", "Ethical", "Geopolitical"]


class TechRiskAssessmentFramework:
    def __init__(self, model: str = "llama3.2"):
        self.model = model
        self.risk_assessments = []
        self.mitigation_strategies = []
    
    def assess_technology_risk(self, technology: str, development_stage: str = "emerging") -> dict:
        prompt = f"""Assess risks of this technology before it's fully developed.

Technology: {technology}
Development Stage: {development_stage}

Return JSON:
{{
    "technology_profile": {{
        "name": "{technology}",
        "stage": "{development_stage}",
        "estimated_timeline": "years to maturity",
        "key_capabilities": ["what it enables"],
        "dual_use_potential": "high/medium/low"
    }},
    "risk_assessment": {{
        "overall_risk_level": "critical/high/medium/low",
        "risk_score": 75,
        "uncertainty_level": "high/medium/low"
    }},
    "risk_categories": [
        {{
            "category": "risk category",
            "risks": [
                {{
                    "risk": "specific risk",
                    "likelihood": "high/medium/low",
                    "severity": "catastrophic/severe/moderate/minor",
                    "timeline": "when could occur",
                    "affected_parties": ["who affected"],
                    "reversibility": "reversible/partially/irreversible"
                }}
            ],
            "category_score": 70
        }}
    ],
    "unintended_consequences": [
        {{
            "consequence": "description",
            "pathway": "how it might happen",
            "warning_signs": ["early indicators"],
            "prevention": "how to prevent"
        }}
    ],
    "misuse_scenarios": [
        {{
            "scenario": "malicious use case",
            "actors": ["who might misuse"],
            "difficulty": "easy/moderate/difficult",
            "impact": "potential damage",
            "countermeasures": ["how to prevent"]
        }}
    ],
    "systemic_risks": {{
        "cascading_failures": ["potential cascades"],
        "dependencies": ["critical dependencies"],
        "single_points_of_failure": ["vulnerabilities"]
    }},
    "existential_considerations": {{
        "x_risk_relevance": "high/medium/low/none",
        "pathways": ["potential paths to x-risk"],
        "safeguards_needed": ["critical safeguards"]
    }},
    "comparison_to_precedents": {{
        "similar_technologies": ["historical parallels"],
        "lessons_learned": ["from past tech"],
        "key_differences": ["why this might be different"]
    }}
}}"""

        response = ollama.chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        result = self._parse_json(response['message']['content'])
        self.risk_assessments.append(result)
        return result
    
    def generate_mitigation_strategies(self, technology: str, risks: List[str]) -> dict:
        prompt = f"""Generate comprehensive risk mitigation strategies.

Technology: {technology}
Identified Risks: {json.dumps(risks)}

Return JSON:
{{
    "mitigation_framework": {{
        "technology": "{technology}",
        "approach": "proactive/reactive/hybrid",
        "governance_model": "recommended governance"
    }},
    "technical_safeguards": [
        {{
            "safeguard": "technical measure",
            "target_risk": "which risk it addresses",
            "implementation": "how to implement",
            "effectiveness": "expected reduction",
            "limitations": ["known limitations"]
        }}
    ],
    "policy_recommendations": [
        {{
            "policy": "policy measure",
            "level": "international/national/industry/organizational",
            "mechanism": "how it works",
            "enforcement": "how enforced",
            "stakeholders": ["responsible parties"]
        }}
    ],
    "governance_structures": {{
        "oversight_bodies": ["recommended bodies"],
        "accountability_mechanisms": ["how to ensure accountability"],
        "transparency_requirements": ["disclosure needs"],
        "public_participation": "how public is involved"
    }},
    "research_priorities": [
        {{
            "priority": "research need",
            "purpose": "why important",
            "timeline": "urgency",
            "funding_needed": "estimated USD"
        }}
    ],
    "early_warning_system": {{
        "indicators": ["what to monitor"],
        "thresholds": ["trigger levels"],
        "response_protocols": ["if threshold exceeded"],
        "responsible_parties": ["who monitors"]
    }},
    "international_coordination": {{
        "need_for_coordination": "high/medium/low",
        "recommended_forums": ["where to coordinate"],
        "treaty_needs": ["international agreements"],
        "enforcement_challenges": ["challenges to address"]
    }},
    "staged_deployment": {{
        "phases": [
            {{
                "phase": "name",
                "conditions": "prerequisites",
                "safeguards": ["required safeguards"],
                "evaluation_criteria": "how to evaluate"
            }}
        ],
        "pause_triggers": ["when to stop development"]
    }},
    "implementation_roadmap": {{
        "immediate_actions": ["next 6 months"],
        "medium_term": ["6-24 months"],
        "long_term": ["2+ years"],
        "cost_estimate": "total USD"
    }}
}}"""

        response = ollama.chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        result = self._parse_json(response['message']['content'])
        self.mitigation_strategies.append(result)
        return result
    
    def analyze_convergence_risks(self, technologies: List[str]) -> dict:
        prompt = f"""Analyze risks from converging technologies.

Converging Technologies: {technologies}

Return JSON:
{{
    "convergence_analysis": {{
        "technologies": {json.dumps(technologies)},
        "convergence_type": "synergistic/additive/enabling"
    }},
    "emergent_capabilities": [
        {{
            "capability": "what becomes possible",
            "contributing_technologies": ["which technologies enable"],
            "timeline": "when possible",
            "impact": "significance"
        }}
    ],
    "synergistic_risks": [
        {{
            "risk": "combined risk",
            "individual_contributions": ["how each tech contributes"],
            "amplification_factor": "how much worse than individual",
            "unique_aspects": ["risks only from combination"]
        }}
    ],
    "cascading_scenarios": [
        {{
            "scenario": "description",
            "trigger": "initiating event",
            "cascade_path": ["sequence of events"],
            "final_impact": "ultimate consequence",
            "intervention_points": ["where to break chain"]
        }}
    ],
    "governance_gaps": [
        {{
            "gap": "what's missing",
            "why_gap_exists": "reason",
            "consequence": "if not addressed",
            "proposed_solution": "how to fill"
        }}
    ],
    "recommendations": {{
        "coordination_needs": ["cross-domain coordination"],
        "integrated_oversight": "unified governance",
        "research_collaboration": "joint research needs"
    }}
}}"""

        response = ollama.chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        return self._parse_json(response['message']['content'])
    
    def horizon_scan(self, time_horizon: int = 10) -> dict:
        prompt = f"""Perform technology horizon scanning for emerging risks.

Time Horizon: {time_horizon} years

Return JSON:
{{
    "horizon_scan": {{
        "time_horizon": "{time_horizon} years",
        "scan_date": "current",
        "methodology": "approach used"
    }},
    "emerging_technologies": [
        {{
            "technology": "name",
            "description": "what it is",
            "emergence_timeline": "years",
            "development_indicators": ["signs of progress"],
            "preliminary_risk_assessment": "initial concerns",
            "monitoring_priority": "high/medium/low"
        }}
    ],
    "wildcards": [
        {{
            "wildcard": "unexpected development",
            "probability": "low/very low",
            "impact_if_occurs": "high/very high",
            "preparation_options": ["how to prepare"]
        }}
    ],
    "megatrends": [
        {{
            "trend": "description",
            "relevance_to_tech_risk": "how it affects risk landscape",
            "implications": ["consequences for risk assessment"]
        }}
    ],
    "priority_watchlist": [
        {{
            "technology": "name",
            "risk_level": "anticipated risk",
            "monitoring_intensity": "frequency",
            "key_metrics": ["what to track"]
        }}
    ],
    "capability_forecast": {{
        "5_years": ["capabilities emerging"],
        "10_years": ["capabilities emerging"],
        "beyond": ["longer-term possibilities"]
    }},
    "recommendations": {{
        "immediate_attention": ["urgent items"],
        "enhanced_monitoring": ["increase surveillance"],
        "preemptive_governance": ["govern before problems"]
    }}
}}"""

        response = ollama.chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        return self._parse_json(response['message']['content'])
    
    def _parse_json(self, content: str) -> dict:
        try:
            start = content.find('{')
            end = content.rfind('}') + 1
            if start != -1 and end > start:
                return json.loads(content[start:end])
        except:
            pass
        return {"raw_response": content}


def display_menu():
    table = Table(title="⚠️ Emergent Technology Risk Assessment", show_header=True)
    table.add_column("Option", style="cyan", width=6)
    table.add_column("Feature", style="green")
    table.add_column("Description", style="white")
    
    table.add_row("1", "Assess Risk", "Assess technology risks")
    table.add_row("2", "Mitigation", "Generate mitigation strategies")
    table.add_row("3", "Convergence", "Analyze converging tech risks")
    table.add_row("4", "Horizon Scan", "Scan for emerging risks")
    table.add_row("5", "View Domains", "List technology domains")
    table.add_row("0", "Exit", "Close application")
    
    console.print(table)


def main():
    console.print(Panel.fit(
        "[bold blue]⚠️ Emergent Technology Risk Assessment Framework[/bold blue]\n"
        "[green]AI-Powered Anticipatory Risk Analysis[/green]\n"
        "[dim]Author: Pranay M[/dim]",
        border_style="blue"
    ))
    
    framework = TechRiskAssessmentFramework()
    
    while True:
        display_menu()
        choice = Prompt.ask("\n[cyan]Select option[/cyan]", default="0")
        
        if choice == "0":
            console.print("[yellow]Goodbye! Anticipate risks, prevent harm! ⚠️[/yellow]")
            break
        
        elif choice == "5":
            console.print("\n[bold]Technology Domains:[/bold]")
            for domain in TECH_DOMAINS:
                console.print(f"  • {domain}")
            continue
        
        with console.status("[bold green]Analyzing risks..."):
            if choice == "1":
                tech = Prompt.ask("Technology to assess")
                stage = Prompt.ask("Development stage", default="emerging")
                result = framework.assess_technology_risk(tech, stage)
                console.print(Panel(Markdown(f"```json\n{json.dumps(result, indent=2)}\n```"),
                                   title="🔍 Risk Assessment"))
            
            elif choice == "2":
                tech = Prompt.ask("Technology")
                risks = Prompt.ask("Key risks (comma-separated)").split(",")
                result = framework.generate_mitigation_strategies(tech, risks)
                console.print(Panel(Markdown(f"```json\n{json.dumps(result, indent=2)}\n```"),
                                   title="🛡️ Mitigation Strategies"))
            
            elif choice == "3":
                techs = Prompt.ask("Technologies (comma-separated)").split(",")
                result = framework.analyze_convergence_risks([t.strip() for t in techs])
                console.print(Panel(Markdown(f"```json\n{json.dumps(result, indent=2)}\n```"),
                                   title="🔗 Convergence Analysis"))
            
            elif choice == "4":
                horizon = IntPrompt.ask("Time horizon (years)", default=10)
                result = framework.horizon_scan(horizon)
                console.print(Panel(Markdown(f"```json\n{json.dumps(result, indent=2)}\n```"),
                                   title="🔭 Horizon Scan"))
        
        console.print("\n" + "="*60)


if __name__ == "__main__":
    main()
