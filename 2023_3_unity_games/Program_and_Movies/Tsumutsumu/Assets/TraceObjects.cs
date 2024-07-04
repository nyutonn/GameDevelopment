using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// GameController に付与されるコンポーネント
public class TraceObjects : MonoBehaviour
{
    // トレースの距離のしきい値
    private float range = 1f;

    // DragLineコンポーネント用の変数
    private DragLine dragLine;

    // トレースを始めた動物のタグ
    private string currentTag;

    // トレースした動物のリスト
    List<GameObject> tracedObjects = new List<GameObject>();

    private void Start(){

        // DragLineコンポーネントの変数
        dragLine = GetComponent<DragLine>();
    
    }

    // トレースを始める
    public void TraceStart(){
        
        // tracedObject を空にする
        tracedObjects.Clear();

        // ゲーム画面上のマウスカーソルの座標を取得する
        Vector3 mousePoint = Camera.main.ScreenToWorldPoint(Input.mousePosition);

        // マウスカーソルの座標における物理的な情報を取得する
        RaycastHit2D hit = Physics2D.Raycast(mousePoint, Vector2.zero);

        // マウスカーソルの座標との接触関係の情報を取得する
        Collider2D indexCollider = hit.collider;

        // マウスカーソルの座標にオブジェクトがあったならば
        if(indexCollider){

            // マウスカーソルの座標にあったオブジェクトを取得する
            GameObject indexObject = indexCollider.gameObject;

            // 取得したオブジェクトのタグがUntagged以外であるならば
            if(indexObject.tag != "Untagged"){

                // 取得したオブジェクトをトレースした動物のリストに追加する
                AddObject(indexObject);

                // currentTag に取得したオブジェクトのタグを代入する
                currentTag = indexObject.tag;

                // 線の開始点を、取得したオブジェクトの座標に設定する
                dragLine.LineStart(hit.transform.position);
            
            }

        }
    }

    // トレースしている
    public void Trace(){

        // ゲーム画面上のマウスカーソルの座標を取得する
        Vector3 mousePoint = Camera.main.ScreenToWorldPoint(Input.mousePosition);

        // マウスカーソルの座標における物理的な情報を取得する
        RaycastHit2D hit = Physics2D.Raycast(mousePoint, Vector2.zero);

        // マウスカーソルの座標との接触関係の情報を取得する
        Collider2D nextCollider = hit.collider;

        // マウスカーソルの座標にオブジェクトがあったならば
        if(nextCollider){

            // マウスカーソルの座標にあったオブジェクトを取得する
            GameObject nextObject = nextCollider.gameObject;

            // 取得したオブジェクトのタグとcurrentTagが等しい かつ nextColliderがCircleCollider2Dである かつ 取得したオブジェクトがトレースされていない ならば
            if(nextCollider.tag == currentTag && nextCollider is CircleCollider2D && !nextObject.GetComponent<BallController>().GetTraced()){

                // nectCollider の CircleCollider2D を代入
                CircleCollider2D col = (CircleCollider2D)nextCollider;

                // トレースしている動物が存在する かつ 取得したオブジェクトと前回にトレースしたオブジェクトの距離が半径*rangeよりも小さい ならば
                if(tracedObjects.Count > 0 && Vector3.Distance(nextCollider.transform.position, tracedObjects[tracedObjects.Count-1].transform.position) <= col.radius * range){
                
                    // 取得したオブジェクトをトレースした動物のリストに追加する
                    AddObject(nextObject);

                    // 前回にトレースしたオブジェクトと取得したオブジェクトの間に線を引く
                    dragLine.DrawLine(hit.transform.position);
                
                }

            }

        }
    }

    // トレースを終える
    public void TraceEnd(){

        // 線を消す
        dragLine.ResetLine();

        // トレースしたオブジェクトのそれぞれに対して
        foreach(GameObject item in tracedObjects){

            // そのオブジェクトをトレースしたかどうかをオフにセットする
            item.GetComponent<BallController>().SetTraced(false);
        
        }

    }

    // オブジェクトをトレースした動物のリストに加える
    private void AddObject(GameObject nextObject){

        // nextObjectをトレースしたかどうかをオンにする
        nextObject.GetComponent<BallController>().SetTraced(true);

        // トレースしたオブジェクトのリストにnextObjectを加える
        tracedObjects.Add(nextObject);
    
    }

    // トレースした動物のリストを返す
    public List<GameObject> GetTracedObjects(){

        // トレースしたオブジェクトが３個以上あるならば
        if(tracedObjects.Count >= 3){

            // トレースしたオブジェクトのリストを返す
            return tracedObjects;
        
        }

        // トレースしたオブジェクトが３個未満であるならば null を返す
        return null;

    }
}