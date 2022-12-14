import unittest
import requests 
import json
import datetime
import os
import sys
import re
import inspect
import string
import random
import logging 
import ast


class SmartTestCase(unittest.TestCase):

    def run(self, result):
        # Store the result on the class so tearDown can behave appropriately
        self.result = result.result if hasattr(result, 'result') else result
        if PY >= (3, 4, 0):
            self._feedErrorsToResultEarly = self._feedErrorsToResult
            self._feedErrorsToResult = lambda *args, **kwargs: None  # no-op
        super(SmartTestCase, self).run(result)

    @property
    def errored(self):
        if (3, 0, 0) <= PY < (3, 4, 0):
            return bool(self._outcomeForDoCleanups.errors)
        return self.id() in [case.id() for case, _ in self.result.errors]

    @property
    def failed(self):
        if (3, 0, 0) <= PY < (3, 4, 0):
            return bool(self._outcomeForDoCleanups.failures)
        return self.id() in [case.id() for case, _ in self.result.failures]

    @property
    def passed(self):
        return not (self.errored or self.failed)

    def tearDown(self):
        if PY >= (3, 4, 0):
            self._feedErrorsToResultEarly(self.result, self._outcome.errors)


class A4AcceptanceTest(SmartTestCase):
    happyCount = 0
    happyFailed = 0
    sadCount = 0
    sadFailed = 0
    extraCreditCount = 0
    extraCreditFailed = 0

    @classmethod
    def setUpClass(cls):   
        cls.instructorURL = "https://rubik-cube.mybluemix.net/rubik"
        cls.testURL = os.environ["url"] + "/rubik"
        cls.userName = os.environ["name"]
        
        cls.cubeKey = 'cube'
        cls.statusKey = 'status'
        cls.statusOk = 'ok' 
        cls.statusError = 'error:'                                   
      
    @classmethod  
    def tearDownClass(cls):
        log.info("----> Assignment4")  
        log.info("      " + os.environ["name"])   
        log.info(f'\tA4: happy path test count --> {A4AcceptanceTest.happyCount}')
        log.info(f'\tA4: happy path tests not passed --> {A4AcceptanceTest.happyFailed}')
        log.info(f'\tA4: sad path test count --> {A4AcceptanceTest.sadCount}')
        log.info(f'\tA4: sad path tests not passed --> {A4AcceptanceTest.sadFailed}')
        # log.info(f'\tA4: extra credit test count --> {A4AcceptanceTest.extraCreditCount}')
        # log.info(f'\tA4: extra credit tests not passed --> {A4AcceptanceTest.extraCreditFailed}')
        log.info("@@@@" + os.environ["name"] + "@@@@" )
 
    def setUp(self):
        super(A4AcceptanceTest, self).setUp()
        log.info('---------------------------------------')
        log.info('RUNNING {} '.format(self.id()))
            
    def tearDown(self):
        def splitCount(caseNumber, count1, count2, count3):
            if(caseNumber < 900):
                count1 += 1
            elif(caseNumber < 990):
                count2 += 1
            else:
                count3 += 1
            return (count1, count2, count3)
                
        super(A4AcceptanceTest, self).tearDown()
        try:
            testNumber = int(re.search(r'(?<=_)\d\d\d+', self.id()).group(0))
            A4AcceptanceTest.happyCount, A4AcceptanceTest.sadCount, A4AcceptanceTest.extraCreditCount = \
                splitCount(testNumber, A4AcceptanceTest.happyCount, A4AcceptanceTest.sadCount, A4AcceptanceTest.extraCreditCount)
            if (self.errored | self.failed):
                A4AcceptanceTest.happyFailed, A4AcceptanceTest.sadFailed, A4AcceptanceTest.extraCreditFailed = \
                    splitCount(testNumber, A4AcceptanceTest.happyFailed, A4AcceptanceTest.sadFailed, A4AcceptanceTest.extraCreditFailed)                
        except:
            log.info('test number invalid ... ignored')
        if self.errored:
            log.info('\tERRORED -----')
        elif self.failed:
            log.info('\tFAILED -----')
        else:
            log.info('\tPASSED -----')
            
# microservice helper methods
    def microservice(self, theURL):
        try:
            log.debug("HTTP request-->" + theURL)
            theResponse = requests.get(theURL)
            log.debug("HTTP response-->" + theResponse.text)
            theResult = ast.literal_eval(theResponse.text)
            theBody = dict(theResult)
            theResult['statusCode'] = theResponse.status_code
        except Exception as e:
            theResult = {}
            theResult['diagnostic1'] = str(e)
            theResult['statusCode'] = 999
            log.error(theResult)
        return theResult 
     
# ------------------------------------------ 

# rubik-specific helper methods

    def invokeMicroservice(self, inputParmDict, theUrl):
        parmString = self.constructParms(inputParmDict)
        theURL = theUrl + '?' + '&'.join(parmString)
        actualResult = self.microservice(theURL)
        statusCode = actualResult.get('statusCode')
        self.assertEqual(200, statusCode, 
                         f'Status of {statusCode} returned from {theURL}')
        actualResult.pop('statusCode')
        return actualResult

    def constructParms(self, parmDict):
        parmString = []
        for key in parmDict:
            parmString.append(key + "=" + parmDict[key])    
        return parmString
    
    def generateColors(self):
        FACES = ['F', 'R', 'B', 'L', 'U', 'D']
        legalCharacters = string.ascii_lowercase + string.ascii_uppercase + string.digits
        randomColors = list((random.sample(legalCharacters, k=6)))
        faceColorDict = dict(zip(FACES, randomColors))
        return faceColorDict     
    
    def generateNominalCube(self, colors):
        ELEMENTS_PER_SIDE = 9
        encodedCube = ""
        for color in colors:
            encodedCube += colors[color] * ELEMENTS_PER_SIDE
        return encodedCube
    
    def scrambleCube(self, encodedCube):
        inputParmDict = {
                            'op': 'solve',
                            'cube': encodedCube,
                         }        
        expectedResult = self.invokeMicroservice(inputParmDict, self.instructorURL) 
        scrambledCube = expectedResult.get('cube', 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy') 
        return scrambledCube
    
    def generateMultipleRotations(self):
        CANDIDATE_ROTATIONS = ['F', 'f',
                               'R', 'r',
                               'B', 'b',
                               'L', 'l',
                               'U', 'u',
                               'D', 'd']
        randomRotations = random.choices(CANDIDATE_ROTATIONS, k=25)
        randomRotationString = "".join(randomRotations)
        return randomRotationString
    
    def extractColors(self, cube):
        FACES = ['F', 'R', 'B', 'L', 'U', 'D']
        positionNumber = 4
        OFFSET = 9
        middles = {}
        for face in FACES:
            middles[cube[positionNumber]] = face
            positionNumber += OFFSET
        return middles
    
    def encodeCube(self, cube, colors):    
        cubeColors = self.extractColors(cube)
        encodedCube = ''
        for cubette in cube:
            encodedCube += colors[cubeColors[cubette]]
        return encodedCube
    
    def isDownFaceCrossA5(self, cube, colors):
        F = '....' + colors['F'] + '..' + colors['F'] + '.'
        R = '....' + colors['R'] + '..' + colors['R'] + '.'
        B = '....' + colors['B'] + '..' + colors['B'] + '.'
        L = '....' + colors['L'] + '..' + colors['L'] + '.'
        U = '....' + colors['U'] + '....'
        D = '.' + colors['D'] + '.' +                                \
                    colors['D'] + colors['D'] + colors['D'] +               \
                    '.' + colors['D'] + '.'
        
        rePattern = F + R + B + L + U + D
        compiledPattern = re.compile(rePattern)
        reResult = compiledPattern.match(cube)
        return reResult
    
    def isDownFaceCross(self, cube, colors):
        F = '....' + colors['F'] + '....' 
        R = '....' + colors['R'] + '....' 
        B = '....' + colors['B'] + '....' 
        L = '....' + colors['L'] + '....' 
        U = '....' + colors['U'] + '....'
        D = '.' + colors['D'] + '.' +                                \
                    colors['D'] + colors['D'] + colors['D'] +               \
                    '.' + colors['D'] + '.'
        
        rePattern = F + R + B + L + U + D
        compiledPattern = re.compile(rePattern)
        reResult = compiledPattern.match(cube)
        return reResult


    def specs(self): 
#-------------------------------------------------------------------------------
# Analysis
#    rubik?op=solve&rotate=R&cube=gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy
#
#    inputs:   can occur in any order
#        op            value of "solve"; mandatory; arrives validated
#        rotate        string consisting of [FfRrBbLlUuDd] or empty string ; 
#                        optional, produces rotation if present and valid, produces solution if missing or empty 
#                        arrives unvalidated
#        cube          string; 54 characters, [azAZ09], 
#                        9 occurrences of 6 characters, 
#                        middle face is each of 6 characters;
#                        mandatory; 
#                        arrives unvalidated
#
#    outputs:
#        side-effects:  no state change; no external effects
#        returns:  JSON string consisting of 
#            nominal if key 'rotate' is missing (in any order)
#                {
#                    'solution':    string consisting of [FfRrBbLlUuDd] or empty string
#                    'status':      'ok'
#                }
#            nominal if key 'rotate' is present (in any order)
#                {
#                    'cube':        54 character serialization of rotated cube
#                    'status':      'ok'
#                }
#            abnormal:
#                {
#                    'status':      'error: xxx' where xxx is dev-selected message, len>0
#                }
#
#    confidence level:  boundary value analysis
#
#    happy path:
#        test 005:  nominal cube with down-facing cross
#        test 010:  nominal scrambled cube with daisy on up face, matching edges
#        test 015:  nominal scrambled cube with daisy on up face, non-matching edges
#        test 020:  nominal scrambled cube with outside down edges
#        test 025:  nominal scrambled cube with facing down edges
#        test 030:  nominal scrambled cube
#        test 035:  nominal scrambled cube; only two keys returned
#        test 040:  nominal scrambled cube, rotation key empty
#        test 045:  nominal scrambled cube, rotation key present
#        test 050:  mixed parm order
#        test 055:  extraneous keys
#
#    sad path:
#        test 905:  missing cube
#        test 910:  short cube
#        test 915:  long cube
#        test 920:  cube with illegal characters, valid otherwise
#        test 925:  cube with != 9 occurrences of at least one of 6 unique characters
#        test 930:  cube with more than 6 unique characters
#        test 935:  cube non-unique middle face
#        test 940:  one key returned under error conditions
#
        pass
    
    def testA4_solve_005_shouldSolveDownCrossOnSolvedCube(self):
#        test 005:   cube with down-facing cross
#                    result:  solution produces cube with down-face cross
        cubeColors = self.generateColors()
        encodedCube = self.generateNominalCube(cubeColors)
        inputParmDict = {
                            'op': 'solve',
                            'cube': encodedCube,
                         }
        
        candidateResult = self.invokeMicroservice(inputParmDict, self.testURL)
        self.assertIn('solution', candidateResult,
                      'fail: ' + inspect.currentframe().f_code.co_name)
        candidateRotations = candidateResult.get('solution')
        
        inputParmDict['rotate'] = candidateRotations
        solutionResult = self.invokeMicroservice(inputParmDict, self.instructorURL) 
        solvedCube = solutionResult['cube']
        self.assertTrue(self.isDownFaceCross(solvedCube, cubeColors),
                        'fail: ' + inspect.currentframe().f_code.co_name)
        
# ------------------------------------------

    def testA4_solve_010_shouldSolveDownCrossOnDownFaceOnTopRowCube(self):
#        test 010:  nominal scrambled cube with daisy on up face, matching edges
#                    result:  solution produces cube with down-face cross
        genericCube = 'gbbgbbgbborrorrorrbggbggbggoorooroorywwwywywwwyyywywyy'
        cubeColors = self.generateColors()
        encodedCube = self.encodeCube(genericCube, cubeColors)

        inputParmDict = {
                            'op': 'solve',
                            'cube': encodedCube,
                         }
        
        candidateResult = self.invokeMicroservice(inputParmDict, self.testURL)
        self.assertIn('solution', candidateResult,
                      'fail: ' + inspect.currentframe().f_code.co_name)
        candidateRotations = candidateResult.get('solution')
        
        inputParmDict['rotate'] = candidateRotations
        solutionResult = self.invokeMicroservice(inputParmDict, self.instructorURL) 
        solvedCube = solutionResult['cube']
        self.assertTrue(self.isDownFaceCross(solvedCube, cubeColors),
                        'fail: ' + inspect.currentframe().f_code.co_name)
        
# ------------------------------------------

    def testA4_solve_015_shouldSolveDownCrossOnUpDaisy(self):
#        test 015:   scrambled cube with daisy on up face, non-matching edges
#                    result:  solution produces cube with down-face cross
        genericCube = 'oororrorrgbbbggbggorrooroorbgggbbgbbwwwwywywyyyyywywyw'
        cubeColors = self.generateColors()
        encodedCube = self.encodeCube(genericCube, cubeColors)

        inputParmDict = {
                            'op': 'solve',
                            'cube': encodedCube,
                         }
        
        candidateResult = self.invokeMicroservice(inputParmDict, self.testURL)
        self.assertIn('solution', candidateResult,
                      'fail: ' + inspect.currentframe().f_code.co_name)
        candidateRotations = candidateResult.get('solution')
        
        inputParmDict['rotate'] = candidateRotations
        solutionResult = self.invokeMicroservice(inputParmDict, self.instructorURL) 
        solvedCube = solutionResult['cube']
        self.assertTrue(self.isDownFaceCross(solvedCube, cubeColors),
                        'fail: ' + inspect.currentframe().f_code.co_name)
        
# ------------------------------------------

    def testA4_solve_020_shouldSolveDownCrossOnOutsideDownEdges(self):
#        test 020:   scrambled cube with outside down edges
#                    result:  solution produces cube with down-face cross
        genericCube = 'gggggggggyowyowyowbbbbbbbbbyrwyrwyrwoooyyyrrrooowwwrrr'
        cubeColors = self.generateColors()
        encodedCube = self.encodeCube(genericCube, cubeColors)

        inputParmDict = {
                            'op': 'solve',
                            'cube': encodedCube,
                         }
        
        candidateResult = self.invokeMicroservice(inputParmDict, self.testURL)
        self.assertIn('solution', candidateResult,
                      'fail: ' + inspect.currentframe().f_code.co_name)
        candidateRotations = candidateResult.get('solution')
        
        inputParmDict['rotate'] = candidateRotations
        solutionResult = self.invokeMicroservice(inputParmDict, self.instructorURL) 
        solvedCube = solutionResult['cube']
        self.assertTrue(self.isDownFaceCross(solvedCube, cubeColors),
                        'fail: ' + inspect.currentframe().f_code.co_name)
        
# ------------------------------------------

    def testA4_solve_025_shouldSolveDownCrossOnFacingDownEdges(self):
#        test 025:   scrambled cube with facing down edges
#                    result:  solution produces cube with down-face cross
        genericCube = 'orwggbggbrobworoororrgbwgbrywgoryyrwbwwgybyybooybwygyw'
        cubeColors = self.generateColors()
        encodedCube = self.encodeCube(genericCube, cubeColors)

        inputParmDict = {
                            'op': 'solve',
                            'cube': encodedCube,
                         }
        
        candidateResult = self.invokeMicroservice(inputParmDict, self.testURL)
        self.assertIn('solution', candidateResult,
                      'fail: ' + inspect.currentframe().f_code.co_name)
        candidateRotations = candidateResult.get('solution')
        
        inputParmDict['rotate'] = candidateRotations
        solutionResult = self.invokeMicroservice(inputParmDict, self.instructorURL) 
        solvedCube = solutionResult['cube']
        self.assertTrue(self.isDownFaceCross(solvedCube, cubeColors),
                        'fail: ' + inspect.currentframe().f_code.co_name)
        
# ------------------------------------------

    def testA4_solve_030_shouldSolveDownCrossOnScrambledCube(self):
#        test 030:  nominal scrambled cube
#                    result:  solution produces cube with down-face cross
        cubeColors = self.generateColors()
        encodedCube = self.generateNominalCube(cubeColors)
        scrambledCube = self.scrambleCube(encodedCube)

        inputParmDict = {
                            'op': 'solve',
                            'cube': scrambledCube,
                         }
        
        candidateResult = self.invokeMicroservice(inputParmDict, self.testURL)
        self.assertIn('solution', candidateResult,
                      'fail: ' + inspect.currentframe().f_code.co_name)
        candidateRotations = candidateResult.get('solution')
        
        inputParmDict['rotate'] = candidateRotations
        solutionResult = self.invokeMicroservice(inputParmDict, self.instructorURL) 
        solvedCube = solutionResult['cube']
        self.assertTrue(self.isDownFaceCross(solvedCube, cubeColors),
                        'fail: ' + inspect.currentframe().f_code.co_name)
        
# ------------------------------------------

    def testA4_solve_035_shouldReturnTwoKeys(self):
#        test 035:  nominal scrambled cube; only two keys returned
#                    result:  solution produces cube with down-face cross
        cubeColors = self.generateColors()
        encodedCube = self.generateNominalCube(cubeColors)
        scrambledCube = self.scrambleCube(encodedCube)

        inputParmDict = {
                            'op': 'solve',
                            'cube': scrambledCube,
                         }
        
        candidateResult = self.invokeMicroservice(inputParmDict, self.testURL)
        returnKeyCount = len(candidateResult)
        self.assertEqual(2, returnKeyCount,
                      'fail: ' + inspect.currentframe().f_code.co_name)
        
# ------------------------------------------

    def testA4_solve_040_shouldSolveOnEmptyRotatekey(self):
#        test 040:  nominal scrambled cube, rotation key empty
#                    result:  solution produces cube with down-face cross
        cubeColors = self.generateColors()
        encodedCube = self.generateNominalCube(cubeColors)
        scrambledCube = self.scrambleCube(encodedCube)

        inputParmDict = {
                            'op': 'solve',
                            'cube': scrambledCube,
                            'rotate': ''
                         }
        
        candidateResult = self.invokeMicroservice(inputParmDict, self.testURL)
        self.assertIn('solution', candidateResult,
                      'fail: ' + inspect.currentframe().f_code.co_name)
        candidateRotations = candidateResult.get('solution')
        
# ------------------------------------------

    def testA4_solve_045_shouldRotateCube(self):
#         test 045:  nominal scrambled cube, rotation key present
#                    result:  solution produces rotated cube
        cubeColors = self.generateColors()
        encodedCube = self.generateNominalCube(cubeColors)
        scrambledCube = self.scrambleCube(encodedCube)
        multipleRotations = self.generateMultipleRotations()
        inputParmDict = {
                            'op': 'solve',
                            'rotate': multipleRotations,
                            'cube': scrambledCube,
                         }
        
        expectedResult = self.invokeMicroservice(inputParmDict, self.instructorURL)        
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)
        
        self.assertDictEqual(expectedResult, actualResult,
                             'fail: ' + inspect.currentframe().f_code.co_name)

# ------------------------------------------

    def testA4_solve_050_shouldIgnoreExtraneousParms(self):
#        test 055:  extraneous keys
#                    result:  solution generated
        cubeColors = self.generateColors()
        encodedCube = self.generateNominalCube(cubeColors)
        scrambledCube = self.scrambleCube(encodedCube)

        inputParmDict = {
                            'op': 'solve',
                            'cube': scrambledCube,
                            'rot': 'ignore me'
                         }
        
        candidateResult = self.invokeMicroservice(inputParmDict, self.testURL)
        self.assertIn('solution', candidateResult,
                      'fail: ' + inspect.currentframe().f_code.co_name)
        
# ------------------------------------------

    def testA4_solve_055_shouldIgnoreParameterOrder(self):
#        test 050:  mixed parm order
#                    result:  solution produces cube with down-face cross
        cubeColors = self.generateColors()
        encodedCube = self.generateNominalCube(cubeColors)
        scrambledCube = self.scrambleCube(encodedCube)

        inputParmDict = {
                            'cube': scrambledCube,
                            'op': 'solve',
                         }
        
        candidateResult = self.invokeMicroservice(inputParmDict, self.testURL)
        self.assertIn('solution', candidateResult,
                      'fail: ' + inspect.currentframe().f_code.co_name)
        
# ------------------------------------------


# ------------------------------------------

    def testA4_solve_905_shouldErrOnMissingCube(self):
#        test 905:  missing cube, nominal rotation
#                    result:  'status': 'error: xxx', where xxx is dev-dependent
        inputParmDict = {
                            'op': 'solve',
                        }

        expectedResult = 'error: '
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)        
        self.assertTrue(actualResult.get('status','').startswith(expectedResult),
                        'fail: ' + inspect.currentframe().f_code.co_name)

# ------------------------------------------

    def testA4_solve_910_shouldErrOnShortCube(self):
#        test 910:  <54 character cube, nominal rotation
#                    result:  'status': 'error: xxx', where xxx is dev-dependent
        inputParmDict = {
                            'op': 'solve',
                            'cube': 'bbbbbbbbbrrrrrrrrrggggggggg',
                        }

        expectedResult = 'error: '
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)        
        self.assertTrue(actualResult.get('status',"").startswith(expectedResult),
                        'fail: ' + inspect.currentframe().f_code.co_name)

# ------------------------------------------

    def testA4_solve_915_shouldErrOnLongCube(self):
#        test 915:  >54 character cube, nominal rotation
#                    result:  'status': 'error: xxx', where xxx is dev-dependent
        inputParmDict = {
                            'op': 'solve',
                            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwww',
                        }

        expectedResult = 'error: '
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)        
        self.assertTrue(actualResult.get('status',"").startswith(expectedResult),
                        'fail: ' + inspect.currentframe().f_code.co_name)

# ------------------------------------------

    def testA4_solve_920_shouldErrOnCubeWithIllegalCharcters(self):
#        test 920:  cube with characters other than [azAZ09], nominal rotation
#                    result:  'status': 'error: xxx', where xxx is dev-dependent
        inputParmDict = {
                            'op': 'solve',
                            'cube': 'bbbbbbbbb         gggggggggoooooooooyyyyyyyyywwwwwwwww',
                        }

        expectedResult = 'error: '
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)        
        self.assertTrue(actualResult.get('status',"").startswith(expectedResult),
                        'fail: ' + inspect.currentframe().f_code.co_name)

# ------------------------------------------

    def testA4_solve_925_shouldErrOnCubeWithIncorrectColorOccurrences(self):
#        test 910:  cube having other than 9 of each color, nominal rotation
#                    result:  'status': 'error: xxx', where xxx is dev-dependent
        inputParmDict = {
                            'op': 'solve',
                            'cube': 'bbbbbbbbbbrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
                        }

        expectedResult = 'error: '
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)        
        self.assertTrue(actualResult.get('status',"").startswith(expectedResult),
                        'fail: ' + inspect.currentframe().f_code.co_name)

# ------------------------------------------

    def testA4_solve_930_shouldErrOnCubeWithOtherThan6UniqueCharacters(self):
#        test 930:  cube having other than 6 of each color, nominal rotatio
#                    result:  'status': 'error: xxx', where xxx is dev-dependent
        inputParmDict = {
                            'op': 'solve',
                            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwe',
                        }

        expectedResult = 'error: '
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)        
        self.assertTrue(actualResult.get('status',"").startswith(expectedResult),
                        'fail: ' + inspect.currentframe().f_code.co_name)

# ------------------------------------------

    def testA4_solve_935_shouldErrOnCubeWithNonUniqueMiddles(self):
#        test 935:  cube with duplicate middle colors, nominal rotation
#                    result:  'status': 'error: xxx', where xxx is dev-dependent
        inputParmDict = {
                            'op': 'solve',
                            'cube': 'bbbbbbbbrrrrrbrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
                        }

        expectedResult = 'error: '
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)        
        self.assertTrue(actualResult.get('status',"").startswith(expectedResult),
                        'fail: ' + inspect.currentframe().f_code.co_name)

# ------------------------------------------

    def testA4_solve_940_shouldReturnOneKeys(self):
#        test 940: one key returned under error conditions
#                    result:  one key return

        inputParmDict = {
                            'op': 'solve',
                         }
        
        candidateResult = self.invokeMicroservice(inputParmDict, self.testURL)
        returnKeyCount = len(candidateResult)
        self.assertEqual(1, returnKeyCount,
                      'fail: ' + inspect.currentframe().f_code.co_name)

# ------------------------------------------

if __name__ == "__main__":
    try:
        os.environ["name"] = "mss0090"
        os.environ["url"] = "http://192.168.1.204:5000/"
        print(" ")
        print("@A4   " + os.environ["name"])      
        # print("      " + os.environ["url"])
        print("      " + str(datetime.datetime.now()))
        print("+------------------------------------------------------------------")    
    except:
        print("@A4  -- identifying information missing")
        sys.exit()
        
    formatter = logging.Formatter(fmt='%(levelname)-8s %(name)s: %(message)s')
    # log_file = os.path.splitext(os.path.abspath(__file__))[0] + '.log'
    log_file = os.environ["name"] + ".log"
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)
    logging.root.addHandler(handler)
    logging.root.setLevel(logging.DEBUG)
    log = logging.getLogger(__name__)
    PY = tuple(sys.version_info)[:3]
    log.info("+------------------------------------------------------------------") 
    log.info("@A4  " + os.environ["name"])  
    # log.info("      " + os.environ["url"])
    log.info("      " + str(datetime.datetime.now()))
    
    unittest.main()
