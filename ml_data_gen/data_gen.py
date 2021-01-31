import random
import time


class HMMDataGen:
    def __init__(self, hmm_datas):
        self.hmm_datas = hmm_datas

    def get_gen(self, data_size=100):
        for i in range(data_size):
            yield self.next()

    def next(self):
        return list(map(lambda hd: hd.next(), self.hmm_datas))


class HMMData:
    def __init__(self, states, hmm_sm, begin_state_index=0, seed=time.time()):
        random.seed(seed)
        self.current_si = begin_state_index
        self.states = [(si, state) for si, state in enumerate(states)]
        self.next_state = self.states[self.current_si][1]
        self.hmm_sm = hmm_sm

    def get_gen(self, data_size=100):
        for i in range(data_size):
            yield self.next()

    def next(self):
        v = self.next_state
        self.current_si, self.next_state = random.choices(self.states, self.hmm_sm[self.current_si])[0]
        return v

    def __str__(self):
        return f"states={self.states}; current si={self.current_si}; next state={self.next_state}:\n{self.hmm_sm}"
