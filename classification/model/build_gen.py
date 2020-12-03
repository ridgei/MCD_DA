import classification.model.svhn2mnist as svhn2mnist
import classification.model.usps as usps
import classification.model.syn2gtrsb as syn2gtrsb


def Generator(source, target, pixelda=False):
    if source == 'usps' or target == 'usps':
        return usps.Feature()
    elif source == 'svhn':
        return svhn2mnist.Feature()
    elif source == 'synth':
        return syn2gtrsb.Feature()


def Classifier(source, target):
    if source == 'usps' or target == 'usps':
        return usps.Predictor()
    if source == 'svhn':
        return svhn2mnist.Predictor()
    if source == 'synth':
        return syn2gtrsb.Predictor()

