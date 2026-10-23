# Zero Trust Network Access (ZTNA) — Educational Policy Simulator
# Educational demonstration only; not a production ZTNA gateway.

from dataclasses import dataclass, asdict
from typing import Dict, List
import pandas as pd

print('ZTNA educational simulator ready')

@dataclass
class AccessRequest:
    user: str
    role: str
    resource: str
    device_managed: bool
    device_compliant: bool
    mfa_verified: bool
    risk_score: int  # illustrative scale: 0 (low) to 100 (high)

ROLE_PERMISSIONS = {
    'student': {'learning_portal'},
    'analyst': {'learning_portal', 'case_dashboard'},
    'admin': {'learning_portal', 'case_dashboard', 'admin_console'},
}

def evaluate_access(req: AccessRequest) -> Dict[str, str]:
    """Return a simple, explainable ZTNA-style decision."""
    if req.resource not in ROLE_PERMISSIONS.get(req.role, set()):
        return {'decision': 'DENY', 'reason': 'Role is not authorized for this resource'}
    if not req.device_managed or not req.device_compliant:
        return {'decision': 'DENY', 'reason': 'Device posture requirements not met'}
    if req.risk_score >= 80:
        return {'decision': 'DENY', 'reason': 'Risk score exceeds the permitted threshold'}
    if not req.mfa_verified or req.risk_score >= 50:
        return {'decision': 'STEP-UP MFA', 'reason': 'Additional verification required'}
    return {'decision': 'ALLOW', 'reason': 'Identity, device, resource, and risk checks passed'}

requests = [
    AccessRequest('Asha', 'student', 'learning_portal', True, True, True, 10),
    AccessRequest('Ravi', 'student', 'admin_console', True, True, True, 5),
    AccessRequest('Mira', 'analyst', 'case_dashboard', True, True, False, 20),
    AccessRequest('Dev', 'analyst', 'case_dashboard', False, False, True, 15),
    AccessRequest('Neel', 'admin', 'admin_console', True, True, True, 88),
    AccessRequest('Ira', 'analyst', 'learning_portal', True, True, True, 55),
    AccessRequest('Kabir', 'guest', 'case_dashboard', True, True, True, 12),
]

results = []
for req in requests:
    decision = evaluate_access(req)
    results.append({**asdict(req), **decision})

df = pd.DataFrame(results)
df

summary = df['decision'].value_counts().rename_axis('decision').reset_index(name='count')
summary

