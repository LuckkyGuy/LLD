import sys, os
sys.path.append(os.path.dirname(__file__))
from issueManagementSystem import IssueManagementSystem
from assignment_strategy import AssignmentStrategy, LeastLoadStrategy
from entites import IssueType, IssueStatus

# Creating issue assignment strategy for IssueManagementSystem.
leastLoadStrategy: AssignmentStrategy = LeastLoadStrategy()

system = IssueManagementSystem.getInstance(leastLoadStrategy)
system.create_issue("T1", IssueType.PAYMENT_RELATED, "Payment Failed", "My payment failed but money is debited", "testUser1@test.com")
system.create_issue("T2", IssueType.MUTUAL_FUND_RELATED, "Purchase Failed", "Unable to purchase Mutual Fund", "testUser2@test.com")
system.create_issue("T3", IssueType.PAYMENT_RELATED, "Payment Failed", "My payment failed but money is debited", "testUser2@test.com")

system.add_agent("agent1@test.com", "Agent 1", [IssueType.PAYMENT_RELATED, IssueType.GOLD_RELATED])
system.add_agent("agent2@test.com", "Agent 2", [IssueType.PAYMENT_RELATED])

# Assigning issues.
print("-------")
system.assign_issue("I1")
system.assign_issue("I2")
system.assign_issue("I3")
print("######")

issue = system.get_issues({"email": "testUser2@test.com"})
system.update_issue("I3", IssueStatus.IN_PROGRESS, "Waiting for payment confirmation")
system.resolve_issue("I3", "Payment Failed, debited amount will get reversed")

# view_agents_work_history
print("-------")
agents_work_history = system.view_agents_work_history()
print("agents_work_history: ", agents_work_history)
print("######")