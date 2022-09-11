import unittest
import rubik.solve as solve


class bottomCrossTest(unittest.TestCase):


    # solving an already solved Cube
    def test_DownCross_010_ShouldReturnStatusOKandSolutionAsNullString(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
    
        expectedResult = {}
        expectedResult['solution'] = ''
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
    
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
        

    # solving an already solved Cube
    def test_DownCross_020_DownCrossSolved(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
    
        expectedResult = True
    
        actualResult = solve._checkIfDownCrossIsSolved(inputDict['cube'])
    
        self.assertEqual(expectedResult, actualResult)
        
    # def test_DownCross_021_DownCrossSolved(self):
    #     inputDict = {}
    #     inputDict['cube'] = 'xxxxxxxxxdRpdRpdRpvvvvvvvvvdzpdzpdzpRRRdddzzzRRRpppzzz'
    #     inputDict['rotate'] = 'FRRuLLfuuuFFRRuuBBuuuLL'
    #     inputDict['op'] = 'solve'
    #
    #     expectedResult = True
    #
    #     actualResult = solve._checkIfDownCrossIsSolved(inputDict['cube'])
    #
    #     self.assertEqual(expectedResult, actualResult)

    # solving an already solved Cube
    def test_DownCross_030_isDaisySolved(self):
        inputDict = {}
        inputDict['cube'] = 'gbggbggbgorooroorobgbbgbbgbrorrorrorywywywywywywywywyw'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
    
        expectedResult = True
    
        actualResult = solve._checkIfDaisyIsSolved(inputDict['cube'])
    
        self.assertEqual(expectedResult, actualResult)
    
    
    
    def test_DownCross_030_findEdgeRotationsLeftPetal(self):
        inputDict = {}
        inputDict['cube'] = 'bgywbgwbgrororoorowbgbgybgyorororrorywgbywywgbywywgbyw'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'bgyybgbbgrororoorowbybgbbgyorrrooorrbwgwywwwgyywywggyw'
        expectedResult['rotate'] = 'l'
        
        actualResultMove = solve._findEdgeRotations(inputDict['cube'], "Left")
        
        inputDict['rotate'] = actualResultMove
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('rotate'), actualResultMove)
        self.assertEqual(expectedResult.get('cube'), actualResult['cube'])
        

    def test_DownCross_031_findEdgeRotationsLeftPetal(self):
        inputDict = {}
        inputDict['cube'] = 'ybbybbybbrrrrrrrrrggwggwggwooooooooogyygyygyybwwbwwbww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'gbbgbbgbbrrrrrrrrrggbggbggbooooooooowyywyywyyywwywwyww'
        expectedResult['rotate'] = 'L'
        
        actualResultMove = solve._findEdgeRotations(inputDict['cube'], "Left")
        
        inputDict['rotate'] = actualResultMove
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('rotate'), actualResultMove)
        self.assertEqual(expectedResult.get('cube'), actualResult['cube'])
        
    
    def test_DownCross_032_findEdgeRotationsFrontPetal(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbyrryrryrrgggggggggoowoowoowyyyyyyooorrrwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'bbbbbbbbborrorrorrgggggggggooroorooryyyyyywwwyyywwwwww'
        expectedResult['rotate'] = 'F'
        
        actualResultMove = solve._findEdgeRotations(inputDict['cube'], "Front")
        
        inputDict['rotate'] = actualResultMove
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('rotate'), actualResultMove)
        self.assertEqual(expectedResult.get('cube'), actualResult['cube'])
        
    def test_DownCross_033_findEdgeRotationsRightPetal(self):
        inputDict = {}
        inputDict['cube'] = 'bbwbbwbbwrrrrrrrrryggyggyggoooooooooyybyybyybwwgwwgwwg'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'bbgbbgbbgrrrrrrrrrbggbggbggoooooooooyywyywyywwwywwywwy'
        expectedResult['rotate'] = 'R'
        
        actualResultMove = solve._findEdgeRotations(inputDict['cube'], "Right")
        
        inputDict['rotate'] = actualResultMove
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('rotate'), actualResultMove)
        self.assertEqual(expectedResult.get('cube'), actualResult['cube'])
        
    def test_DownCross_034_findEdgeRotationsBackPetal(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrwrrwrrwgggggggggyooyooyoorrryyyyyywwwwwwooo'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'bbbbbbbbbrrorrorrogggggggggroorooroowwwyyyyyywwwwwwyyy'
        expectedResult['rotate'] = 'B'
        
        actualResultMove = solve._findEdgeRotations(inputDict['cube'], "Back")
        
        inputDict['rotate'] = actualResultMove
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('rotate'), actualResultMove)
        self.assertEqual(expectedResult.get('cube'), actualResult['cube'])
        
        

    def test_DownCross_035_findFaceRotationsLeftPetal(self):
        inputDict = {}
        inputDict['cube'] = 'rbbwbbwbbyrryrryrrggoggyggywwwoooooobyybyyboogrrgwwgww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'ybbbbobbwyrryrrorrggrggggggbboooroorwyywyygooyybwwwwww'
        expectedResult['rotate'] = 'LuFU'
        
        actualResultMove = solve._findFaceRotations(inputDict['cube'], "Left")
        
        inputDict['rotate'] = actualResultMove
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('rotate'), actualResultMove)
        self.assertEqual(expectedResult.get('cube'), actualResult['cube'])
        
    def test_DownCross_036_findFaceRotationsFrontPetal(self):
        inputDict = {}
        inputDict['cube'] = 'wwwbbbbbbgrrwrrwrryggyggyggoobooyooyyybyybrrrooowwgwwg'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'rrbbbgbbgyrrrrbrrwyggyggbggoogooooooyybyybwwowwywwywwr'
        expectedResult['rotate'] = 'FuRU'
        
        actualResultMove = solve._findFaceRotations(inputDict['cube'], "Front")
        
        inputDict['rotate'] = actualResultMove
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('rotate'), actualResultMove)
        self.assertEqual(expectedResult.get('cube'), actualResult['cube'])
        
    def test_DownCross_037_findFaceRotationsRightPetal(self):
        inputDict = {}
        inputDict['cube'] = 'bbrbbybbywwwrrrrrroggwggwggyooyooyoorrgyygyygwwbwwboob'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'bbobbbbbbggrrrorroyggggrggwyooyooroorrbyywyywwwwwwwgyy'
        expectedResult['rotate'] = 'RuBU'
        
        actualResultMove = solve._findFaceRotations(inputDict['cube'], "Right")
        
        inputDict['rotate'] = actualResultMove
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('rotate'), actualResultMove)
        self.assertEqual(expectedResult.get('cube'), actualResult['cube'])
    
    def test_DownCross_038_findFaceRotationsBackPetal(self):
        inputDict = {}
        inputDict['cube'] = 'ybbybbybbrrgrryrrywwwggggggboowoowooooogyygyybwwbwwrrr'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'ybbybbgbbrrbrrrrrroogggbggbyoooogoowrwwgyygyyowwywwyww'
        expectedResult['rotate'] = 'BuLU'
        
        actualResultMove = solve._findFaceRotations(inputDict['cube'], "Back")
        
        inputDict['rotate'] = actualResultMove
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('rotate'), actualResultMove)
        self.assertEqual(expectedResult.get('cube'), actualResult['cube'])
    
    

    def test_DownCross_040_SolveDaisyBack(self):
        inputDict = {}
        inputDict['cube'] = 'gbggbggbgrrorrorrobgbbgbbgbrooroorooyyywywwwwyyyywywww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
    
        expectedResult = {}
        expectedResult['cube'] = 'gbggbggbgrrrrrrrrrbgbbgbbgbooooooooowwwwywwwwyyyywyyyy'
        expectedResult['solution'] = 'BB'
    
        actualResult = solve._solveForDaisyPetals(inputDict['cube'])
    
        self.assertEqual(expectedResult.get('solution'), actualResult[0])
        self.assertEqual(expectedResult.get('cube'), actualResult[1])
        
        
    def test_DownCross_041_SolveDaisy(self):
        inputDict = {}
        inputDict['cube'] = 'ybbybbybbrrrrrrrrrggwggwggwooooooooogyygyygyybwwbwwbww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
    
        expectedFrontPetal = "w"
        expectedLeftPetal = "w"
        expectedRightPetal = "w"
        expectedBackPetal = "w"
        
        actualResult = solve._solveForDaisyPetals(inputDict['cube'])
        actualCube = actualResult[1]
        actualFrontPetal = actualCube[43]
        actualLeftPetal = actualCube[39]
        actualRightPetal = actualCube[41]
        actualBackPetal = actualCube[37]
        
        self.assertEqual(expectedFrontPetal, actualFrontPetal)
        self.assertEqual(expectedLeftPetal, actualLeftPetal)
        self.assertEqual(expectedRightPetal, actualRightPetal)
        self.assertEqual(expectedBackPetal, actualBackPetal)
        
    #
    def test_DownCross_042_SolveDaisy(self):
        inputDict = {}
        inputDict['cube'] = 'wwwbbbgggbrrwrryooyggyggyggrobroyrowwwbwybrrooooywbyyb'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
    
        expectedFrontPetal = "w"
        expectedLeftPetal = "w"
        expectedRightPetal = "w"
        expectedBackPetal = "w"
    
        actualResult = solve._solveForDaisyPetals(inputDict['cube'])
        actualCube = actualResult[1]
        actualFrontPetal = actualCube[43]
        actualLeftPetal = actualCube[39]
        actualRightPetal = actualCube[41]
        actualBackPetal = actualCube[37]
    
        self.assertEqual(expectedFrontPetal, actualFrontPetal)
        self.assertEqual(expectedLeftPetal, actualLeftPetal)
        self.assertEqual(expectedRightPetal, actualRightPetal)
        self.assertEqual(expectedBackPetal, actualBackPetal)
    
    
    def test_DownCross_043_SolveDownCrossFromPetal(self):
        inputDict = {}
        inputDict['cube'] = 'bggybgybgrooorrooowbbygbygyrrrrooorrywbwywwwwgywgwbgyb'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
    
        expectedFrontAdjacentColor = "b"
        expectedRightAdjacentColor = "r"
        expectedBackAdjacentColor = 'g'
        expectedLeftAdjacentColor = 'o'
        
        
        expectedFrontPetal = "w"
        expectedLeftPetal = "w"
        expectedRightPetal = "w"
        expectedBackPetal = "w"
        
        actualResult = solve._solveForDownCrossFromSolvedDaisy(inputDict['cube'])
        actualCube = actualResult[1]
        actualFrontPetal = actualCube[46]
        actualLeftPetal = actualCube[48]
        actualRightPetal = actualCube[50]
        actualBackPetal = actualCube[52]
        
        actualFrontAdjacentCell = actualCube[7]
        actualRightAdjacentCell = actualCube[16]
        actualBackAdjacentCell = actualCube[25]
        actualLeftAdjacentCell = actualCube[34]
        
        # Checking Front DownCross petal and adjacentFace
        self.assertEqual(expectedFrontPetal, actualFrontPetal)
        self.assertEqual(expectedFrontAdjacentColor, actualFrontAdjacentCell)
        
        # Checking Right DownCross petal and adjacentFace
        self.assertEqual(expectedRightPetal, actualRightPetal)
        self.assertEqual(expectedRightAdjacentColor, actualRightAdjacentCell)
        
        # Checking Back DownCross petal and adjacentFace
        self.assertEqual(expectedBackPetal, actualBackPetal)
        self.assertEqual(expectedBackAdjacentColor, actualBackAdjacentCell)
        
        # Checking Left DownCross petal and adjacentFace
        self.assertEqual(expectedLeftPetal, actualLeftPetal)
        self.assertEqual(expectedLeftAdjacentColor, actualLeftAdjacentCell)
        
        
        
        
    # solving an already solved Cube
    def test_DownCross_050_AutoSolve(self):
        inputDict = {}
        inputDict['cube'] = 'ybbybbybbrrrrrrrrrggwggwggwooooooooogyygyygyybwwbwwbww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        
        resultFromDaisy = solve._solveForDaisyPetals(inputDict['cube'])
        daisyCube = resultFromDaisy[1]
        daisyMoves = resultFromDaisy[0]
        resultFromDownCross = solve._solveForDownCrossFromSolvedDaisy(daisyCube)
        DownCrossCube = resultFromDownCross[1]
        DownCrossMoves = resultFromDownCross[0]
        
        expectedMoves = daisyMoves + DownCrossMoves
        expectedResult = ""
        
        actualResultMoves = solve._autoSolveCube(inputDict['cube'])
    
        self.assertIsNot(expectedResult, actualResultMoves)
        self.assertEqual(expectedMoves, actualResultMoves)
        

    # solving an already solved Cube
    def test_DownCross_060_SolveDownCrossFromScrambledCubeCorrectStatus(self):
        inputDict = {}
        inputDict['cube'] = 'bggybgybgrooorrooowbbygbygyrrrrooorrywbwywwwwgywgwbgyb'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
    
        expectedResult = {}
        expectedResult['rotate'] = None
        expectedResult['cube'] = None
        expectedResult['solution'] = ''
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
    
        self.assertIsNot(expectedResult.get('solution'), actualResult.get('solution'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        self.assertEqual(expectedResult.get('rotate'), actualResult.get('rotate'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        
        
    # solving an already solved Cube
    def test_DownCross_070_ShouldErrorInvalidCube(self):
        inputDict = {}
        inputDict['cube'] = 'bggybgybgrooorrooowbbygbygyrrrrooorrywbwywwwwgywgwbgy'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
    
        expectedResult = {}
        expectedResult['rotate'] = None
        expectedResult['cube'] = None
        expectedResult['solution'] = ''
        expectedResult['status'] = 'error: cube string length is not 54 its 53'
    
        actualResult = solve._solve(inputDict)
    
        self.assertIsNot(expectedResult.get('solution'), actualResult.get('solution'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        self.assertEqual(expectedResult.get('rotate'), actualResult.get('rotate'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        