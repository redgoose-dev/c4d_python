# Create object
#
# 이 스크립트를 실행하면 메뉴를 선택하여 오브젝트를 만들 수 있습니다.
# 오브젝트를 추가하려면 menuNames list값을 수정하면 됩니다.

import c4d
from c4d import gui

# menu Tree
menuNames = ['null', 'cube', 'sphere', 'figure']
menuTree = {}
for i,v in enumerate(menuNames):
    menuTree[c4d.FIRST_POPUP_ID + i] = v


# create Object
def createObject(str):
    unit = c4d.BaseObject(eval('c4d.O' + str))
    unit.SetName('my' + str)
    
    if str != 'null':
        tag_phong = c4d.BaseTag(c4d.Tphong)
        tag_phong[c4d.PHONGTAG_PHONG_ANGLELIMIT] = True
        unit.InsertTag(tag_phong)
    
    return unit


# MAIN
def main():
    
    doc.StartUndo()
    
    menu = c4d.BaseContainer()
    for o in menuTree.items():
        menu.SetString(o[0], o[1])

    result = gui.ShowPopupDialog(cd=None, bc=menu, x=c4d.MOUSEPOS, y=c4d.MOUSEPOS)

    if result:
        obj = createObject(menuTree[result])
        doc.InsertObject(obj)
        doc.AddUndo(c4d.UNDOTYPE_NEW, obj)

    doc.EndUndo()
    c4d.EventAdd()


if __name__=='__main__':
    main()
