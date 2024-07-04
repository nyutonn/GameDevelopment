using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// GameController に付与されるコンポーネント
public class Timer : MonoBehaviour
{
    // 経過時間を保持するカウンター変数
    private float counter;

    // カウント中であるかどうか
    private bool counting;


    // 最初のフレームが始まる直前に実行される処理
    private void Start(){
        counter = 0f;
    }

    // フレーム毎に実行される処理
    private void Update(){
        if(counting){
            counter += Time.deltaTime;
        }
    }

    // カウンターの経過時間を0秒にリセットする
    public void ResetCounter(){
        counter = 0f;
    }

    // カウントを始める
    public void StartCounter(){
        counting = true;
    }

    // カウントを止める
    public void StopCounter(){
        counting = false;
    }

    // カウンターの経過時間を返す
    public float GetCountTime(){
        return counter;
    }
}