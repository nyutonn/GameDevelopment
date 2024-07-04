using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// 動物に付与されているコンポーネント
public class BallController : MonoBehaviour
{
	// 動物がトレースされたかどうか
    private bool traced;
    

    // 動物のトレースを設定する
    public void SetTraced(bool traced){
        this.traced = traced;
    }

    // 動物がトレースされたかどうかを返す
    public bool GetTraced(){
        return traced;
    }
}