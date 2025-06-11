class Nodes:
    def __init__(self, probability, symbol, left=None, right=None):
        self.probability = probability
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ''


def calculateProbability(the_data):
    the_symbols = dict()
    for item in the_data:
        if the_symbols.get(item) is None:
            the_symbols[item] = 1
        else:
            the_symbols[item] += 1
    return the_symbols


the_codes = dict()


def calculateCodes(node, value=''):
    newValue = value + str(node.code)
    if node.left:
        calculateCodes(node.left, newValue)
    if node.right:
        calculateCodes(node.right, newValue)
    if not node.left and not node.right:
        the_codes[node.symbol] = newValue
    return the_codes


def OutputEncoded(the_data, coding):
    encodingsOutput = []
    for element in the_data:
        encodingsOutput.append(coding[element])
    the_string = ''.join([str(item) for item in encodingsOutput])
    return the_string


def TotalGain(the_data, coding):
    beforCompression = len(the_data) * 8
    afterCompression = 0
    the_symbols = coding.keys()
    for symbol in the_symbols:
        the_count = the_data.count(symbol)
        afterCompression += the_count * len(coding[symbol])
    print('space usage before compression (in bits)', beforCompression)
    print('space usage after compression (in bits)', afterCompression)


def HuffmanEncoding(the_data):
    symbolWithProbs = calculateProbability(the_data)
    the_symbols = symbolWithProbs.keys()
    the_probabilities = symbolWithProbs.values()
    print('symbols', the_symbols)
    print('probabilities', the_probabilities)

    the_nodes = []

    for symbol in the_symbols:
        the_nodes = sorted(the_nodes, key=lambda x: x.probability)
    while len(the_nodes) > 1:
        the_nodes = sorted(the_nodes, key=lambda x: x.probability)
