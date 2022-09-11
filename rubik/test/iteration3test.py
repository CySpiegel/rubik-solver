import unittest
import rubik.solve as solve
from rubik.solve import _isLowerLevelSolved

class iteration3Test(unittest.TestCase):

    def test_lowerLevelSolve_010_ShouldReturnTrueforBottomSolved(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
    
        expectedResult = True
        
    
        actualResult = solve._isLowerLevelSolved(inputDict['cube'])
    
        self.assertEqual(expectedResult, actualResult)
        
    
    def test_lowerLevelSolve_910_ShouldReturnFalseforBottomSolved(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrorrorrogggggggggroorooroowwwyyyyyywwwwwwyyy'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
    
        expectedResult = False
        actualResult = solve._isLowerLevelSolved(inputDict['cube'])
    
        self.assertEqual(expectedResult, actualResult)
        
    def test_lowerLevelSolve_911_ShouldReturnFalseforBottomSolved(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbooorrrrrrbbbggggggrrroooooogggyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
    
        expectedResult = False
        actualResult = solve._isLowerLevelSolved(inputDict['cube'])
    
        self.assertEqual(expectedResult, actualResult)


    def test_lowerLevelSolve_020_ShouldReturnCubeFrontFaceRightTrigger(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        
        inputTriggerDirection = "RightTrigger"
        inputSelectedFace = "Front"
        inputMoveLIst = ""
    
        expectedResult = {}
        expectedResult['cube'] = 'rrybbybbbgrrgrryrrgooggggggbbwooooooyyyyyybbowwrwwwwww'
        expectedResult['status'] = 'ok'
        expectedMoveList = "RUr"
    
        actualMoveList, actualCube = solve._triggerAction(inputDict['cube'], inputTriggerDirection, inputSelectedFace, inputMoveLIst)
    
        self.assertEqual(expectedResult['cube'], actualCube)
        self.assertEqual(expectedMoveList, actualMoveList)
        

    def test_lowerLevelSolve_021_ShouldReturnCubeFrontFaceLeftTrigger(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        
        inputTriggerDirection = "LeftTrigger"
        inputSelectedFace = "Front"
        inputMoveLIst = ""
    
        expectedResult = {}
        expectedResult['cube'] = 'yooybbbbbwbbrrrrrrrrgggggggoogoogooyyyyyyyrbbowwwwwwww'
        expectedResult['status'] = 'ok'
        expectedMoveList = "luL"
    
        actualMoveList, actualCube = solve._triggerAction(inputDict['cube'], inputTriggerDirection, inputSelectedFace, inputMoveLIst)
    
        self.assertEqual(expectedResult['cube'], actualCube)
        self.assertEqual(expectedMoveList, actualMoveList)
        
        
    def test_lowerLevelSolve_022_ShouldReturnCubeRightFaceRightTrigger(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        
        inputTriggerDirection = "RightTrigger"
        inputSelectedFace = "Right"
        inputMoveLIst = ""
    
        expectedResult = {}
        expectedResult['cube'] = 'rrwbbbbbbggyrryrrroggoggyggobbooooooyybyyryyrwwwwwwwwg'
        expectedResult['status'] = 'ok'
        expectedMoveList = "BUb"
    
        actualMoveList, actualCube = solve._triggerAction(inputDict['cube'], inputTriggerDirection, inputSelectedFace, inputMoveLIst)
    
        self.assertEqual(expectedResult['cube'], actualCube)
        self.assertEqual(expectedMoveList, actualMoveList)
    
    
    def test_lowerLevelSolve_023_ShouldReturnCubeBackFaceRightTrigger(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        
        inputTriggerDirection = "RightTrigger"
        inputSelectedFace = "Back"
        inputMoveLIst = ""
    
        expectedResult = {}
        expectedResult['cube'] = 'brrbbbbbbggwrrrrrrooyggygggboobooyoorggyyyyyywwwwwwoww'
        expectedResult['status'] = 'ok'
        expectedMoveList = "LUl"
    
        actualMoveList, actualCube = solve._triggerAction(inputDict['cube'], inputTriggerDirection, inputSelectedFace, inputMoveLIst)
    
        self.assertEqual(expectedResult['cube'], actualCube)
        self.assertEqual(expectedMoveList, actualMoveList)
        
    def test_lowerLevelSolve_024_ShouldReturnCubeLeftFaceRightTrigger(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        
        inputTriggerDirection = "RightTrigger"
        inputSelectedFace = "Left"
        inputMoveLIst = ""
    
        expectedResult = {}
        expectedResult['cube'] = 'rbbrbbybbrggrrrrrroowggggggbbyooyooooyyoyygyybwwwwwwww'
        expectedResult['status'] = 'ok'
        expectedMoveList = "FUf"
    
        actualMoveList, actualCube = solve._triggerAction(inputDict['cube'], inputTriggerDirection, inputSelectedFace, inputMoveLIst)
    
        self.assertEqual(expectedResult['cube'], actualCube)
        self.assertEqual(expectedMoveList, actualMoveList)
        

    def test_lowerLevelSolve_025_ShouldReturnCubeRightFaceLeftTrigger(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        
        inputTriggerDirection = "LeftTrigger"
        inputSelectedFace = "Right"
        inputMoveLIst = ""
    
        expectedResult = {}
        expectedResult['cube'] = 'bbobbobbyybbyrrrrrwrrggggggggoooooooyyryyryygwwbwwwwww'
        expectedResult['status'] = 'ok'
        expectedMoveList = "fuF"
    
        actualMoveList, actualCube = solve._triggerAction(inputDict['cube'], inputTriggerDirection, inputSelectedFace, inputMoveLIst)
    
        self.assertEqual(expectedResult['cube'], actualCube)
        self.assertEqual(expectedMoveList, actualMoveList)
        
        
    def test_lowerLevelSolve_026_ShouldReturnCubeBackFaceLeftTrigger(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        
        inputTriggerDirection = "LeftTrigger"
        inputSelectedFace = "Back"
        inputMoveLIst = ""
    
        expectedResult = {}
        expectedResult['cube'] = 'oobbbbbbbrrbrrbrryyrrygggggwggooooooggoyyyyyywwwwwwwwr'
        expectedResult['status'] = 'ok'
        expectedMoveList = "ruR"
    
        actualMoveList, actualCube = solve._triggerAction(inputDict['cube'], inputTriggerDirection, inputSelectedFace, inputMoveLIst)
    
        self.assertEqual(expectedResult['cube'], actualCube)
        self.assertEqual(expectedMoveList, actualMoveList)
        
    def test_lowerLevelSolve_027_ShouldReturnCubeLeftFaceLeftTrigger(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        
        inputTriggerDirection = "LeftTrigger"
        inputSelectedFace = "Left"
        inputMoveLIst = ""
    
        expectedResult = {}
        expectedResult['cube'] = 'woobbbbbbbbrrrrrrrggrggrggyyggyooooobyyoyyoyywwwwwwgww'
        expectedResult['status'] = 'ok'
        expectedMoveList = "buB"
    
        actualMoveList, actualCube = solve._triggerAction(inputDict['cube'], inputTriggerDirection, inputSelectedFace, inputMoveLIst)
    
        self.assertEqual(expectedResult['cube'], actualCube)
        self.assertEqual(expectedMoveList, actualMoveList)
        
    def test_lowerLevelSolve_030_ShouldDetectCorner1Solved(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        bottomCell = 45
        
        expectedResult = True
        
        actualResult = solve._isCornerSolved(inputDict['cube'], bottomCell)
    
        self.assertEqual(expectedResult, actualResult)
    
    def test_lowerLevelSolve_031_ShouldDetectCorner2Solved(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        bottomCell = 47
        
        expectedResult = True
        
        actualResult = solve._isCornerSolved(inputDict['cube'], bottomCell)
    
        self.assertEqual(expectedResult, actualResult)
        
    def test_lowerLevelSolve_032_ShouldDetectCorner3Solved(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        bottomCell = 51
        
        expectedResult = True
        
        actualResult = solve._isCornerSolved(inputDict['cube'], bottomCell)
    
        self.assertEqual(expectedResult, actualResult)

    def test_lowerLevelSolve_033_ShouldDetectCorner4Solved(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        bottomCell = 53
        
        expectedResult = True
        
        actualResult = solve._isCornerSolved(inputDict['cube'], bottomCell)
    
        self.assertEqual(expectedResult, actualResult)
        

    def test_lowerLevelSolve_930_ShouldDetectCorner1NotSolved(self):
        inputDict = {}
        inputDict['cube'] = 'wbbwbbwbbrrrrrrrrrggyggyggyooooooooobyybyybyygwwgwwgww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        bottomCell = 45
        
        expectedResult = False
        
        actualResult = solve._isCornerSolved(inputDict['cube'], bottomCell)
    
        self.assertEqual(expectedResult, actualResult)
        

    def test_lowerLevelSolve_040_DetectWhiteCellsInCornerGroup(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        lookAtCell = 45
        
        expectedResult = True
        
        actualResult = solve._DetectWhiteCellsInCornerGroup(inputDict['cube'], lookAtCell)
    
        self.assertEqual(expectedResult, actualResult)
        

    def test_lowerLevelSolve_041_DetectWhiteCellsInCornerGroup(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        lookAtCell = 36
        
        expectedResult = False
        
        actualResult = solve._DetectWhiteCellsInCornerGroup(inputDict['cube'], lookAtCell)
    
        self.assertEqual(expectedResult, actualResult)


    def test_lowerLevelSolve_050_moveWhitetInBottomCornerGroupsIfNotSolved(self):
        inputDict = {}
        inputDict['cube'] = 'rryybybbogbbrrrbrrrogggggggyowoogooyryybyybboowwwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        moveList = ""
        
        expectedResult = {}
        expectedResult['cube'] = "brrybybbygbborrorrrowggggggrrwoogooybbybyyoyyowgwwwwww"
        
        actualResult = solve._moveWhitetInBottomCornerGroupsIfNotSolved(inputDict['cube'], moveList)
    
        self.assertEqual(expectedResult['cube'], actualResult[1])

    def test_lowerLevelSolve_051_moveWhitetInBottomCornerGroupsIfNotSolvedWithWhiteAbove47(self):
        inputDict = {}
        inputDict['cube'] = 'yowybybborryrrrbrrgbbggggggrogoogooyyyoyybrbbowwwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        moveList = ""
        
        expectedResult = {}
        expectedResult['cube'] = "brrybybbygbborrorrrowggggggrrwoogooybbybyyoyyowgwwwwww"
        expectedMoveList = "URUr"
        actualResult = solve._moveWhitetInBottomCornerGroupsIfNotSolved(inputDict['cube'], moveList)
    
        self.assertEqual(expectedResult['cube'], actualResult[1])
        self.assertEqual(expectedMoveList, actualResult[0])
        

    def test_lowerLevelSolve_052_moveWhitetInBottomCornerGroupsIfNotSolvedWithWhiteAbove(self):
        inputDict = {}
        inputDict['cube'] = 'woyrbyrbbooobrgyrgwryrgoogyryryoyoobgbbgybggbwwrwwwgww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        moveList = ""
        
        expectedResult = {}
        expectedResult['cube'] = "worgbyobbwowbrryrybggbgoggywybyoyoobororygrbgywrwwwgwr"
        expectedMoveList = "UluLUUruR"
        actualResult = solve._moveWhitetInBottomCornerGroupsIfNotSolved(inputDict['cube'], moveList)
        
        
        self.assertEqual(expectedResult['cube'], actualResult[1])
        self.assertEqual(expectedMoveList, actualResult[0])
        
        

    def test_lowerLevelSolve_060_ShouldSolveLastCornerToBottom(self):
        inputDict = {}
        inputDict['cube'] = 'yywbbybbyrrybrrbrrgybggggggrogooooooygoyybrrbwwowwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        moveList = ""
    
        expectedResult = {}
        expectedResult['cube'] = "yyrbbobbbyyyyrrrrrorygggggggygooooooobbgybrrbwwwwwwwww"
        expectedMoveList = "fuF"
        
        actualResult = solve._moveWhiteCornersFromTopToBottom(inputDict['cube'], moveList)
        

        self.assertEqual(expectedResult['cube'], actualResult[1])
        self.assertEqual(expectedMoveList, actualResult[0])
        

    def test_lowerLevelSolve_061_ShouldSolveLastCornerToBottom(self):
        inputDict = {}
        inputDict['cube'] = 'rrybbybbygybbrrbrrrogggggggyywooooooryyrygbbowwowwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        moveList = ""
    
        expectedResult = {}
        expectedResult['cube'] = "yyrbbobbbyyyyrrrrrorygggggggygooooooobbgybrrbwwwwwwwww"
        expectedMoveList = "UUUfuF"
        
        actualResult = solve._moveWhiteCornersFromTopToBottom(inputDict['cube'], moveList)
        
        self.assertEqual(expectedResult['cube'], actualResult[1])
        self.assertEqual(expectedMoveList, actualResult[0])
        

    def test_lowerLevelSolve_062_ShouldSolveWithMultipleUnlovedCorners(self):
        inputDict = {}
        inputDict['cube'] = 'wgbobyobbworgryyrrwrwbgyygobbgroyyoyobgoygorrgwrwwwbwg'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        moveList = ""
    
        expectedResult = {}
        expectedResult['cube'] = "ryggbgbbbybyrrrrrrorgygbgggoybooooooybbgyyyorwwwwwwwww"

        
        actualResult = solve._moveWhiteCornersFromTopToBottom(inputDict['cube'], moveList)
        
        self.assertEqual(expectedResult['cube'], actualResult[1])

    
    
    def test_lowerLevelSolve_070_DetectColersAboveLowerCornerMatchTheThreeColorsExpectedInLowerCorner(self):
        inputDict = {}
        inputDict['cube'] = 'bbwbbybbbrrygrryrrgrrgggggggooooooooyyoyybyybwwrwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        lookAtCell = 47
        
        expectedResult = True
        
        actualResult = solve._cornerColorsAboveMatchExpecetedBottomCornerColors(inputDict['cube'], lookAtCell)
    
        self.assertEqual(expectedResult, actualResult)
    
    def test_lowerLevelSolve_070_ShouldReturnFalseIfAboveCornerDoesNotMatchExpectedColorSet(self):
        inputDict = {}
        inputDict['cube'] = 'bbwbbybbbrrygrryrrgrrgggggggooooooooyyoyybyybwwrwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        lookAtCell = 45
        
        expectedResult = False
        
        actualResult = solve._cornerColorsAboveMatchExpecetedBottomCornerColors(inputDict['cube'], lookAtCell)
    
        self.assertEqual(expectedResult, actualResult)
        
        
    def test_lowerLevelSolve_080_ShouldSolveLastCornerToBottomWhenWiteIsOnTopFaceOfCubeCorner(self):
        inputDict = {}
        inputDict['cube'] = 'ygrbbybbybryorrgrrorygggggggbrooooooobbyyybywwwrwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        moveList = ""
    
        expectedResult = {}
        expectedResult['cube'] = "gbbbbybbbyrbrrrrrrrgrgggggggoyooooooyyyyyboyowwwwwwwww"
        expectedMoveList = "RUUruRUr"
        
        actualResult = solve._moveWhiteCornersFromTopToBottom(inputDict['cube'], moveList)
        
        self.assertEqual(expectedResult['cube'], actualResult[1])
        self.assertEqual(expectedMoveList, actualResult[0])
        
    def test_lowerLevelSolve_081_ShouldSolveLastCornerToBottomWhenWiteIsOnTopFaceOfCubeCorner(self):
        inputDict = {}
        inputDict['cube'] = 'ggorbbybywbgorygrbrgboggogywboroyoobrowyyrwybrwrwwwgwy'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        moveList = ""
    
        expectedResult = {}
        expectedResult['cube'] = "rrygbrbbbooybrbrrrgbyogygggrrbgooooogyogyyyybwwwwwwwww"

        
        actualResult = solve._moveWhiteCornersFromTopToBottom(inputDict['cube'], moveList)
        
        self.assertEqual(expectedResult['cube'], actualResult[1])

        
        
    
    def test_lowerLevelSolve_082_ShouldSolveLowerLevelOfCubeFromSolvedBottomCross(self):
        inputDict = {}
        inputDict['cube'] = 'ggorbbybywbgorygrbrgboggogywboroyoobrowyyrwybrwrwwwgwy'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
    
        expectedResult = "UFUfUUURUUruRUrULUUluLUlUBUb"
        
        
        actualResult = solve._autoSolveCube(inputDict['cube'])
    
        self.assertEqual(expectedResult, actualResult)
        
        
    def test_lowerLevelSolve_083_ShouldSolveLowerLevelOfCubeFromScambledCube(self):
        inputDict = {}
        inputDict['cube'] = 'bggybgybgrooorrooowbbygbygyrrrrooorrywbwywwwwgywgwbgyb'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
    
        expectedResult = {}
        expectedResult["status"] = 'ok'
                
        actualResult = solve._solve(inputDict)

        self.assertEqual(expectedResult["status"], actualResult['status'])