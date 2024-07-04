using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// GameController に付与されるコンポーネント
public class DragLine : MonoBehaviour
{
    // LineRendererコンポーネントの変数
    private LineRenderer lineRenderer;

    // 線のカウンター
    private int counter;

    // 最初のフレームが始まる直前に実行される処理
    private void Start(){

        // LineRendererコンポーネントを取得する
        lineRenderer = gameObject.GetComponent<LineRenderer>();

        // 線をリセットする
        ResetLine();

    }

    // 線をリセットする
    public void ResetLine(){
        counter = 0;
        lineRenderer.positionCount = 0;
    }

    // 線の開始点を設定する
    public void LineStart(Vector3 startPoint){
        counter = 0;
        lineRenderer.positionCount = 1;
        startPoint.z = -1;
        lineRenderer.SetPosition(counter, startPoint);
    }

    // 線を引く
    public void DrawLine(Vector3 currentPoint){
        counter++;
        lineRenderer.positionCount++;
        currentPoint.z = -1;
        lineRenderer.SetPosition(counter, currentPoint);
    }
}