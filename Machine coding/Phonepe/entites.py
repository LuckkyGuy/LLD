import sys, os
sys.path.append(os.path.dirname(__file__))
from enum import Enum

class Issue:
    def __init__(self, issue_id, transaction_id, issue_type, subject, description, email):
        self.issue_id = issue_id
        self.transaction_id = transaction_id
        self.issue_type = issue_type
        self.subject = subject
        self.description = description
        self.email = email
        self.status = IssueStatus.OPEN
        self.resolution = None
        self.assigned_agent = None

    def update_status(self, status, resolution=None):
        self.status = status
        self.resolution = resolution
        
    def assign_agent(self, agent):
        self.assigned_agent = agent


class Agent:
    def __init__(self, email, name, expertise):
        self.email = email
        self.name = name
        self.expertise = expertise  # List of issue types
        self.current_issue = None
        self.work_history = []

    def assign_issue(self, issue):
        if self.current_issue is None:
            self.current_issue = issue
            issue.assign_agent(self)
            self.work_history.append(issue)
            return True
        return False

    def resolve_current_issue(self, resolution):
        if self.current_issue:
            self.current_issue.update_status(IssueStatus.RESOLVED, resolution)
            self.current_issue = None

class IssueType(Enum):
    PAYMENT_RELATED = "Payment Related"
    MUTUAL_FUND_RELATED = "Mutual Fund Related"
    GOLD_RELATED = "Gold Related"
    INSURANCE_RELATED = "Insurance Related"

class IssueStatus(Enum):
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"




Agent
Issue
system time stamp
time : issues
Agent : issue