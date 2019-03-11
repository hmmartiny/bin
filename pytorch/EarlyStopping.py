class EarlyStopping(object):
    """Checks if the network has not been improving
    
    Inspired by the many answers in the following thread: https://discuss.pytorch.org/t/early-stopping-in-pytorch/18800
    """

    def __init__(self, patience, mode):
        self.patience = patience
        self.best_score = None
        self.mode = mode
        self.counter = 0
        self.stop = False

    def step(self, score):
        """Check score of last epoch"""
        if self.best_score is None:
            self.best_score = score
        
        else:
            if self.mode == 'max':
                self.max_mode(score)
            elif self.mode == 'min':
                self.min_mode(score)
            else:
                raise AssertionError("mode '{}' not found".format(self.mode))

            if self.counter >= self.patience:
                self.stop = True
        
    def max_mode(self, score):

        # update if score has been improved
        if score > self.best_score:
            self.best_score = score
            self.score = 0 # reset
        
        # if not, then update counter
        elif score < self.best_score:
            self.counter += 1
    
    def min_mode(self, score):

        # update if score has been improved
        if score < self.best_score:
            self.best_score = score
            self.score = 0 # reset
        
        # if not, then update counter
        elif score > self.best_score:
            self.counter += 1            
