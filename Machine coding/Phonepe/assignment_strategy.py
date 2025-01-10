import sys, os
sys.path.append(os.path.dirname(__file__))

from abc import ABC, abstractmethod

class AssignmentStrategy(ABC):
    @abstractmethod
    def assign_issue(self, issue, agents):
        pass


class RoundRobinStrategy(AssignmentStrategy):
    def __init__(self):
        self.last_assigned_index = -1

    def assign_issue(self, issue, agents):
        available_agents = [agent for agent in agents if issue.issue_type in agent.expertise and agent.current_issue is None]
        if not available_agents:
            print("No available agent, issue added to waitlist")
            return False

        self.last_assigned_index = (self.last_assigned_index + 1) % len(available_agents)
        selected_agent = available_agents[self.last_assigned_index]
        selected_agent.assign_issue(issue)
        print(f"Issue {issue.issue_id} assigned to agent {selected_agent.name}")
        return True
    
class LeastLoadStrategy(AssignmentStrategy):
    def assign_issue(self, issue, agents):
        available_agents = [agent for agent in agents if issue.issue_type in agent.expertise and agent.current_issue is None]
        if not available_agents:
            print("No available agent, issue added to waitlist")
            return False

        selected_agent = min(available_agents, key=lambda agent: len(agent.work_history))
        selected_agent.assign_issue(issue)
        print(f"Issue {issue.issue_id} assigned to agent {selected_agent.name}")
        return True
