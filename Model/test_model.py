from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model
from load_images import MoleImages
from sklearn.metrics import classification_report
from sklearn.metrics import roc_curve, auc
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import sys

def plot_roc(y_test, y_score, title='ROC Curve'):
    fpr, tpr, _ = roc_curve(y_test, y_score)
    roc_auc = auc(fpr, tpr)
    print(roc_auc)
    plt.figure()
    lw = 2
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(title)
    plt.legend(loc="lower right")
    plt.savefig(title + '.png')
    plt.show()


if __name__ == '__main__':
    mimg = MoleImages()
    test = sys.argv[ ]
    # X_test, y_test = mimg.load_test_images('data/benign/images',
    #                                            'data/malign/images')
    img = mpimg.imread(test)
    model = load_model('benigns.h5')
    model.load_weights(model)
    pred_proba = model.predict(img)
    # y_pred = (y_pred_proba >0.5)*1
    print(pred_proba)
    # plot_roc(y_test, y_pred_proba, title=sys.argv[1]+sys.argv[2])
    
