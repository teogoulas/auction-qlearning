class Action:

    def __init__(self, agent: int, agent1_action: int, agent2_action: int):
        self._agent = agent
        self._agent1_action = agent1_action
        self._agent2_action = agent2_action

    @property
    def agent(self) -> int:
        return self._agent

    @property
    def agent1_action(self) -> int:
        return self._agent1_action

    @property
    def agent2_action(self) -> int:
        return self._agent2_action
