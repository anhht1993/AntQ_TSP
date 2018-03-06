class AntQGraph:

    def __init__(self, heu_mat, aq_mat=None):
        self.aq_mat = aq_mat
        self.heu_mat = heu_mat
        if aq_mat is None:
            self.aq_mat = self.heu_mat
        self.num_node = len(self.aq_mat)

    def antQ_val(self, r, s):
        return self.aq_mat[r][s]

    def heu_val(self, r, s):
        return self.heu_mat[r][s]

    def distance(self, r, s):
        distance = 1.0 / self.heu_val(r, s)
        return distance




