import sys, os
sys.path.append(os.path.dirname(__file__))
from entites import Issue, Agent
from assignment_strategy import AssignmentStrategy
from collections import deque

class IssueManagementSystem:
    __shared_instance = None
    
    @staticmethod
    def getInstance(strategy):
        if not IssueManagementSystem.__shared_instance:
            IssueManagementSystem(strategy)
        return IssueManagementSystem.__shared_instance
    
    def __init__(self, strategy):
        if IssueManagementSystem.__shared_instance:
            raise Exception("This class is a Singleton class !")
        else:
            IssueManagementSystem.__shared_instance = self
            self.issues = {}
            self.agents = {}
            self.issue_id_counter = 1
            self.unassigned_issues = deque() 
            self.strategy = strategy


    def create_issue(self, transaction_id, issue_type, subject, description, email):
        issue_id = f"I{self.issue_id_counter}"
        self.issue_id_counter += 1
        issue = Issue(issue_id, transaction_id, issue_type, subject, description, email)
        self.issues[issue_id] = issue
        return issue_id

    def add_agent(self, email, name, expertise):
        agent = Agent(email, name, expertise)
        self.agents[email] = agent

    def assign_issue(self, issue_id):
        issue= self.issues.get(issue_id)
        if not issue:
            return "Issue not found"

        issue_assignment_status = self.strategy.assign_issue(issue, list(self.agents.values()))
        if issue_assignment_status ==False:
            # No agent available, put in waitlist
            self.unassigned_issues.append(issue)

    def get_issues(self, filter_criteria,):
        filtered_issues= []
        for issue in self.issues.values():
            match = all(getattr(issue, key) == value for key, value in filter_criteria.items())
            if match:
                filtered_issues.append(issue)
        return filtered_issues

    def update_issue(self, issue_id, status, resolution):
        issue = self.issues.get(issue_id)
        if issue:
            issue.update_status(status, resolution)

    def resolve_issue(self, issue_id, resolution):
        issue= self.issues.get(issue_id)
        if issue and issue.assigned_agent:
            issue.assigned_agent.resolve_current_issue(resolution)

    def view_agents_work_history(self):
        return {agent.name: [issue.issue_id for issue in agent.work_history] for agent in self.agents.values()}


