import numpy
from scipy.stats.stats import chisquare
from scipy.spatial.distance import cdist
from StatUtils import binaryValue
from sklearn.metrics import matthews_corrcoef
class ParamCorrelation(object):

    _analyzedCommits = []

    _isSubjectLt50CharValues = []
    _subjectEndsWithoutDotValues = []
    _subjectStartWithCapitalLetterValues = []
    _isSubjectInImperativeMoodValues = []
    _isBodyWrappedAt72CharsValues = []
    _subjectLineSeparatedFromBodyValues = []
    _isBodyExplenatoryValues = []

    _corr_s50_noDot = None
    _corr_s50_cap = None
    _corr_s50_b72 = None
    _corr_s50_slb = None
    _corr_s50_imp = None
    _corr_s50_exp = None

    _corr_noDot_cap = None
    _corr_noDot_b72 = None
    _corr_noDot_slb = None
    _corr_noDot_Imp = None
    _corr_noDot_exp = None

    _corr_cap_b72 = None
    _corr_cap_slb = None
    _corr_cap_imp = None
    _corr_cap_exp = None

    _corr_b72_slb = None
    _corr_b72_imp = None
    _corr_b72_exp = None

    _corr_slb_imp = None
    _corr_slb_exp = None

    _corr_imp_exp = None

    def __init__(self, analyzedCommits):
        self._analyzedCommits = analyzedCommits

    def extractData(self):
        for commit in self._analyzedCommits:
            self._isSubjectLt50CharValues.append(binaryValue(commit._isSubjectLt50Char))
            self._subjectEndsWithoutDotValues.append(binaryValue(commit._subjectEndsWithoutDot))
            self._subjectStartWithCapitalLetterValues.append(binaryValue(commit._subjectStartWithCapitalLetter))
            self._isSubjectInImperativeMoodValues.append(binaryValue(commit._isSubjectInImperativeMood))
            self._isBodyWrappedAt72CharsValues.append(binaryValue(commit._isBodyWrappedAt72Chars))
            self._subjectLineSeparatedFromBodyValues.append(binaryValue(commit._subjectLineSeparatedFromBody))
            # self._isBodyExplenatoryValues.append(commit._)

    def countCorrelation(self):
        self.correl_S50_NoDot()
        self.correl_s50_cap()
        self.correl_s50_b72()
        self.correl_s50_slb()
        self.correl_s50_imp()
        # self.correl_s50_exp()
        self.correl_noDot_cap()
        self.correl_noDot_b72()
        self.correl_noDot_slb()
        self.correl_noDot_Imp()
        # self.correl_noDot_exp()
        self.correl_cap_b72()
        self.correl_cap_slb()
        self.correl_cap_imp()
        # self.correl_cap_exp()
        self.correl_b72_slb()
        self.correl_b72_imp()
        # self.correl_b72_exp()
        self.correl_slb_imp()
        # self.correl_slb_exp()
        # self.correl_imp_exp()

    def correl_S50_NoDot(self):
        self._corr_s50_noDot = matthews_corrcoef(self._isSubjectLt50CharValues, self._subjectEndsWithoutDotValues)

    def correl_s50_cap(self):
        self._corr_s50_cap = matthews_corrcoef(self._isSubjectLt50CharValues, self._subjectStartWithCapitalLetterValues)

    def correl_s50_b72(self):
        self._corr_s50_b72 = matthews_corrcoef(self._isSubjectLt50CharValues, self._isBodyWrappedAt72CharsValues)

    def correl_s50_slb(self):
        self._corr_s50_slb = matthews_corrcoef(self._isSubjectLt50CharValues, self._subjectLineSeparatedFromBodyValues)

    def correl_s50_imp(self):
        self._corr_s50_imp = matthews_corrcoef(self._isSubjectLt50CharValues, self._isSubjectInImperativeMoodValues)

    def correl_s50_exp(self):
        raise NotImplementedError("Not implemented part - body explanatory")

    def correl_noDot_cap(self):
        self._corr_noDot_cap = matthews_corrcoef(self._subjectEndsWithoutDotValues, self._subjectStartWithCapitalLetterValues)

    def correl_noDot_b72(self):
        self._corr_noDot_b72 = matthews_corrcoef(self._subjectEndsWithoutDotValues, self._isBodyWrappedAt72CharsValues)

    def correl_noDot_slb(self):
        self._corr_noDot_slb = matthews_corrcoef(self._subjectEndsWithoutDotValues, self._subjectLineSeparatedFromBodyValues)

    def correl_noDot_Imp(self):
        self._corr_noDot_Imp = matthews_corrcoef(self._subjectEndsWithoutDotValues, self._isSubjectInImperativeMoodValues)

    def correl_noDot_exp(self):
        raise NotImplementedError("Not implemented part - body explanatory")

    def correl_cap_b72(self):
        self._corr_cap_b72 = matthews_corrcoef(self._subjectStartWithCapitalLetterValues, self._isBodyWrappedAt72CharsValues)

    def correl_cap_slb(self):
        self._corr_cap_slb = matthews_corrcoef(self._subjectStartWithCapitalLetterValues, self._subjectLineSeparatedFromBodyValues)

    def correl_cap_imp(self):
        self._corr_cap_imp = matthews_corrcoef(self._subjectStartWithCapitalLetterValues, self._isSubjectInImperativeMoodValues)

    def correl_cap_exp(self):
        raise NotImplementedError("Not implemented part - body explanatory")

    def correl_b72_slb(self):
        self._corr_b72_slb = matthews_corrcoef(self._isBodyWrappedAt72CharsValues, self._subjectLineSeparatedFromBodyValues)

    def correl_b72_imp(self):
        self._corr_b72_imp = matthews_corrcoef(self._isBodyWrappedAt72CharsValues, self._isSubjectInImperativeMoodValues)

    def correl_b72_exp(self):
        raise NotImplementedError("Not implemented part - body explanatory")

    def correl_slb_imp(self):
        self._corr_slb_imp = matthews_corrcoef(self._subjectLineSeparatedFromBodyValues, self._isSubjectInImperativeMoodValues)

    def correl_slb_exp(self):
        raise NotImplementedError("Not implemented part - body explanatory")

    def correl_imp_exp(self):
        raise NotImplementedError("Not implemented part - body explanatory")

    def __str__(self):
            return(
                        "S50 - NoDot: " +  str(self._corr_s50_noDot) + "\n" +
                        "S50 - Cap: " +  str(self._corr_s50_cap) + "\n" +
                        "S50 - B72: " +  str(self._corr_s50_b72) + "\n" +
                        "S50 - SLB: " +  str(self._corr_s50_slb) + "\n" +
                         "S50 - Imp: " +  str(self._corr_s50_imp) + "\n"+
                        "NoDot - Cap: " +  str(self._corr_noDot_cap) + "\n" +
                        "NoDot - B72: " +  str(self._corr_noDot_b72) + "\n" +
                        "NoDot - SLB: " +  str(self._corr_noDot_slb) + "\n" +
                        "NoDot - Imp: " +  str(self._corr_noDot_Imp) + "\n" +
                        "Cap - B72: " +  str(self._corr_cap_b72) + "\n" +
                        "Cap - SLB: " +  str(self._corr_cap_slb) + "\n" +
                        "Cap - Imp: " +  str(self._corr_cap_imp) + "\n" +
                        "B72 - SLB: " +  str(self._corr_b72_slb) + "\n"
                        "B72 - IMP: " +  str(self._corr_b72_imp) + "\n"
                        "SLB - IMP: " +  str(self._corr_slb_imp) + "\n"
            )