import QtQuick 1.1
Rectangle {
    id:r
    anchors.centerIn: parent
    width: 200
    height: 200
    Column{
        width: r.width*0.8
        height: r.height*0.8
        spacing: 10
        anchors.centerIn: parent
        Row{
            id:ro
            spacing:10
            Text {
                anchors.centerIn: ro.parent
                font.bold: true
                text: "a"
            }
            TextInput {
                id: a
                width: r.width*3/4
                height: 20
                selectionColor: "#2f8bc5"
                fillColor: "lightgray"
                font.bold: true
            }
        }
        Row{
            spacing:10
        Text {
            text: "b"
            font.bold: true
        }
        TextInput {
            id: b
            width: r.width*3/4
            height: 20
            fillColor: "lightgray"
            font.bold: true
        }
        }
        Rectangle {
            id: calculate
            width: r.width
            height: 30
            color: "#8a0800"
            //x:b.width*0.2
            Text{
                anchors.centerIn: calculate
                font.bold: true
                text:"calculate";color:"white"}
                gradient: Gradient {
                GradientStop {
                    position: 0
                    color: "#8a0800"
                }
                GradientStop {
                    position: 1
                    color: "#330009"
                }
            }
        }

        Row{
            spacing:10
        Text {
            text: "c"
            font.bold: true
        }
        TextInput {
            id: c
            font.bold: true
            width: r.width*3/4
            height: 20
            fillColor: "lightgray"
            selectionColor: "#2f8bc5"
            font.pixelSize: 12
        }
        }
    }
}
