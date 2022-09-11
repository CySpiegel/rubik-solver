import unittest
import rubik.solve as solve

class iteration4Test(unittest.TestCase):

    def test_middlelayerSolved_010_ShouldReturnTrueforMIddleLayerSolved(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
    
        expectedResult = True
        
        actualResult = solve._isMiddleLayerSolved(inputDict['cube'])
    
        self.assertEqual(expectedResult, actualResult)
        
    def test_middlelayerSolved_011_ShouldReturnFalseforMIddleLayerNotSolved(self):
        inputDict = {}
        inputDict['cube'] = 'bbbobbbbbyggrrrrrryrygggggggyyoobooooyroyyryowwwwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
    
        expectedResult = False

        actualResult = solve._isMiddleLayerSolved(inputDict['cube'])
    
        self.assertEqual(expectedResult, actualResult)
        
    def test_middlelayerSolved_012_ShouldReturnFalseforMIddleLayerNotSolved(self):
        inputDict = {}
        inputDict['cube'] = 'bggybgybgrooorrooowbbygbygyrrrrooorrywbwywwwwgywgwbgyb'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
    
        expectedResult = False

        actualResult = solve._isMiddleLayerSolved(inputDict['cube'])
    
        self.assertEqual(expectedResult, actualResult)
        

    def test_topDaisyHasYellow_020_ShouldReturnTrueIfTopDaisyHasYellowInPedals(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
    
        expectedResult = True

        actualResult = solve._isYellowInTopEdge(inputDict['cube'])
    
        self.assertEqual(expectedResult, actualResult)
        
    def test_topDaisyHasYellow_021_ShouldReturnFalseIfTopDaisyHasNoYellowInPedals(self):
        inputDict = {}
        inputDict['cube'] = 'bggybgybgrooorrooowbbygbygyrrrrooorrywbwywwwwgywgwbgyb'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
    
        expectedResult = False

        actualResult = solve._isYellowInTopEdge(inputDict['cube'])
    
        self.assertEqual(expectedResult, actualResult)
        
        
    def test_moveEdgeToMatchingFaceColor_030_ShouldNotModifyCubeState(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        
        inputEdgeColor = 'b'
        inputMoves = ""
        inputFaceColorList = ['b', 'r', 'g', 'o']
        
        expectedCube = "bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww"

        actualCube, MovesMade  = solve._moveEdgeToMatchingFaceColor(inputDict['cube'], inputEdgeColor, inputFaceColorList, inputMoves)
        self.assertEqual(expectedCube, actualCube)
        

    def test_moveEdgeToMatchingFaceColor_031_ShouldModifyCubeState(self):
        inputDict = {}
        inputDict['cube'] = 'ooobbbbbbbbbrrrrrrrrrgggggggggooooooyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        
        inputEdgeColor = 'o'
        inputMoves = ""
        inputFaceColorList = ['b', 'r', 'g', 'o']
        
        expectedCube = "bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww"
        expectedMoves = 'uuu'
        actualCube, MovesMade  = solve._moveEdgeToMatchingFaceColor(inputDict['cube'], inputEdgeColor, inputFaceColorList, inputMoves)
        
        self.assertEqual(expectedMoves, MovesMade)
        self.assertEqual(expectedCube, actualCube)
        
    
    def test_moveTopEdgeToSolvedPossition_040_ShouldModifyCubeState(self):
        inputDict = {}
        inputDict['cube'] = 'orobbgbbbyryyryrrrbbgogggggyryooooooryrgybbygwwwwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        
        inputEdgePair = ['r', 'b']
        inputMoves = ""
        inputFaceColorList = ['Right','r', 'g', 'o', 'b']
        
        expectedCube = "oyrbbbbbbgrorryrrryrbogggggrgyooooooyggyyybbywwwwwwwww"
        expectedMoves = 'ufuFURUr'
        actualCube, MovesMade  = solve._moveTopEdgeToSolvedPossition(inputDict['cube'], inputEdgePair, inputFaceColorList, inputMoves)
        
        self.assertEqual(expectedMoves, MovesMade)
        self.assertEqual(expectedCube, actualCube)

    
    
    # def test_solveForMIddleLayer_050_ShouldReturnTrueForSolvedCube(self):
    #     inputDict = {}
    #     inputDict['cube'] = 'yoybbbbbbbybrrgrrrybyrgggggrgooooooogyoyyrgyrwwwwwwwww'
    #     inputDict['rotate'] = ''
    #     inputDict['op'] = 'solve'
    #
    #     inputMoves = ""
    #
    #     expectedResult = True
    #
    #     MovesMade, actualCube = solve._solveForMIddleLayer(inputDict['cube'], inputMoves)
    #     actualResultIsSolved = solve._isMiddleLayerSolved(inputDict['cube'])
    #     print(actualCube)
    #     self.assertEqual(expectedResult, actualResultIsSolved)
        

    def test_solveForMIddleLayer_051_ShouldReturnTrueForSolvedCube(self):
        inputDict = {}
        inputDict['cube'] = 'byybbybbbrygorrrrrorrggggggybooooooobbyyygyrgwwwwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
    
        inputMoves = ""
    
        expectedResult = True
    
        MovesMade, actualCube = solve._solveForMIddleLayer(inputDict['cube'], inputMoves)
        actualResultIsSolved = solve._isMiddleLayerSolved(actualCube)
        self.assertEqual(expectedResult, actualResultIsSolved)
        
    def test_solveForMIddleLayer_052_ShouldReturnTrueForSolvedCube(self):
        inputDict = {}
        inputDict['cube'] = 'yrgbbybbborgoryrrryrrbgggggyyboooooobbrgyyogywwwwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
    
        inputMoves = ""
    
        expectedResult = True
    
        MovesMade, actualCube = solve._solveForMIddleLayer(inputDict['cube'], inputMoves)
        actualResultIsSolved = solve._isMiddleLayerSolved(actualCube)
        self.assertEqual(expectedResult, actualResultIsSolved)
        

    def test_solveForMIddleLayer_053_ShouldReturnTrueForSolvedCube(self):
        inputDict = {}
        inputDict['cube'] = 'oogybgbbbyryyrrrrrbboggggggbrgooboooyorbyyyyrwwwwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
    
        inputMoves = ""
    
        expectedResult = True
    
        MovesMade, actualCube = solve._solveForMIddleLayer(inputDict['cube'], inputMoves)
        actualResultIsSolved = solve._isMiddleLayerSolved(actualCube)
        self.assertEqual(expectedResult, actualResultIsSolved)
        
        
    def test_solve_060_ShouldReturnStatusofOK(self):
        inputDict = {}
        inputDict['cube'] = 'oogybgbbbyryyrrrrrbboggggggbrgooboooyorbyyyyrwwwwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
    
        expectedResult = {}
        expectedResult["status"] = 'ok'
                
        actualResult = solve._solve(inputDict)

        self.assertEqual(expectedResult["status"], actualResult['status'])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        