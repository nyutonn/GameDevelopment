using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// GameController に付与されるコンポーネント
public class Score : MonoBehaviour
{
    // スコアを保持する変数
    private int score;


    // 最初のフレームが始まる直前に実行される処理
    private void Start(){
        score = 0;
    }

    // フレーム毎に実行される処理
    public int GetScore(){
        return score;
    }

    // スコアをセット
    public void SetScore(int score){
        this.score = score;
    }

    // スコアに足す
    public void AddScore(int score){
        this.score += score;
    }
}