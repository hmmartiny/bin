import numpy as np

def results_to_log(date, net, epochs, lr, acc_train, mcc_train, auc_train, loss_train, acc_test, mcc_test, auc_test, loss_test, early_stopping, filename):
    """Append the network results to a log file"""
    with open(filename, 'a') as f:
        f.write("#"*100)
        f.write("\nNetwork ran date: {} and trained on {} epochs with lr={}\n".format(date, epochs, lr))
        f.write(net.__str__())
        f.write("\nTrain Accuracy: {:.3f}, MCC: {:.3f}, AUC: {:.3f}, loss: {:.3f}, perplexity: {:.3f}\n".format(acc_train, mcc_train, auc_train, loss_train, np.exp(loss_train)))
        f.write("Valid Accuracy: {:.3f}, MCC: {:.3f}, AUC: {:.3f}, loss: {:.3f}, perplexity: {:.3f}\n".format(acc_test, mcc_test, auc_test, loss_test, np.exp(loss_test)))
        f.write("Early stopped: {}\n".format(early_stopping))
    
    print("Results appended to file:", filename)