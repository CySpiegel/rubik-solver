import unittest
import rubik.solve as solve


class debugtesting(unittest.TestCase):
    # def test_DownCross_010_ShouldReturnStatusOKandSolutionAsNullString(self):
    #     inputDict = {}
    #     inputDict['cube'] = 'QxuyuQyxWXyXWWxyyyQWQXxXWuuuQxuXXXxXWuxXQWWQyxyuWyuQQx'
    #     inputDict['rotate'] = ''
    #     inputDict['op'] = 'solve'
    #
    #     expectedResult = {}
    #     expectedResult['solution'] = ''
    #     expectedResult['status'] = 'ok'
    #
    #     actualResult = solve._solve(inputDict)
    #
    #     self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
    #     self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    
    def test_lowerLevelSolve_052_moveWhitetInBottomCornerGroupsIfNotSolvedWithWhiteAbove(self):
        inputDict = {}
        inputDict['cube'] = 'woyrbyrbbooobrgyrgwryrgoogyryryoyoobgbbgybggbwwrwwwgww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        moveList = ""
    
        expectedResult = {}
        expectedResult['cube'] = ""
        expectedMoveList = ""
        actualResult = solve._moveWhitetInBottomCornerGroupsIfNotSolved(inputDict['cube'], moveList)
    
        print(actualResult[1])
        print("Moves: ", actualResult[0])
    
        self.assertEqual(expectedResult['cube'], actualResult[1])
        self.assertEqual(expectedMoveList, actualResult[0])
    


        

    # def test_lowerLevelSolve_930_ShouldDetectCorner1NotSolved(self):
    #     inputDict = {}
    #     inputDict['cube'] = 'woyrbyrbbooobrgyrgwryrgoogyryryoyoobgbbgybggbwwrwwwgww'
    #     inputDict['rotate'] = ''
    #     inputDict['op'] = 'solve'
    #     bottomCell = 53
    #
    #     expectedResult = False
    #
    #     actualResult = solve._isCornerSolved(inputDict['cube'], bottomCell)
    #
    #     self.assertEqual(expectedResult, actualResult)
    

    # def test_lowerLevelSolve_040_DetectWhiteCellsInCornerGroup(self):
    #     inputDict = {}
    #     inputDict['cube'] = 'woyrbyrbbooobrgyrgwryrgoogyryryoyoobgbbgybggbwwrwwwgww'
    #     inputDict['rotate'] = ''
    #     inputDict['op'] = 'solve'
    #     lookAtCell = 53
    #
    #     expectedResult = True
    #
    #     actualResult = solve._DetectWhiteCellsInCornerGroup(inputDict['cube'], lookAtCell)
    #
    #     self.assertEqual(expectedResult, actualResult)