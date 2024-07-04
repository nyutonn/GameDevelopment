using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

// GameController に付与されるコンポーネント
public class GameController : MonoBehaviour
{
    // 残り時間のテキスト
    private Text countTimeText;

    // プログレスサークル（残り時間）のイメージ
    private Image remainTimeImage;

    // スコアのテキスト
    private Text scoreText;

    // タイムアップのキャンバス
    private Canvas timeUpCanvas;

    // トータルスコアのテキスト
    private Text totalScoreText;

    // 最初に生成するボールの個数
    private int startNumber = 25;

    // 制限時間
    private float timeLimit = 60f;

    // SpawnControllerコンポーネントの変数
    private SpawnController spawnController;

    // 次に生成する動物プレハブの個数
    private int nextSpawnNumber;

    // TraceObjectsコンポーネントの変数
    private TraceObjects traceObjects;

    // Timerコンポーネントの変数
    private Timer timer;

    // 経過時間
    private float countTime;

    // 残り時間
    private float remainTime;

    // Scoreコンポーネントの変数
    private Score score;

    // ゲームが終了したかどうか
    private bool gameSet;


    // 最初のフレームが始まる直前に実行される処理
    private void Start(){

        // SpawnControllerコンポーネントを取得する
        spawnController = GetComponent<SpawnController>();

        // TraceObjectsコンポーネントを取得する
        traceObjects = GetComponent<TraceObjects>();

        // Timerコンポーネントを取得する
        timer = GetComponent<Timer>();

        // Scoreコンポーネントを取得する
        score = GetComponent<Score>();

        // スコアのテキストを取得する
        scoreText = GameObject.Find("GameCanvas/Text").GetComponent<Text>();

        // 残り時間のテキストを取得する
        countTimeText = GameObject.Find("GameCanvas/Timer/Text").GetComponent<Text>();

        // プログレスサークル（残り時間）のイメージを取得する
        remainTimeImage = GameObject.Find("GameCanvas/Timer/Remain").GetComponent<Image>();

        // 経過時間を0秒に初期化
        countTime = 0f;

        // タイムアップのキャンバスを取得する
        timeUpCanvas = GameObject.Find("TimeUpCanvas").GetComponent<Canvas>();

        // トータルスコアのテキストを取得する
        totalScoreText = GameObject.Find("TimeUpCanvas/Text").GetComponent<Text>();

        // タイムアップUIを非表示にする
        timeUpCanvas.enabled = false;

        // スコアのテキストにスコアをセットする
        SetScoreText();

        // startNumber（個）の動物プレハブを生成する
        spawnController.Spawn(startNumber);

        // タイマーをリセットする
        timer.ResetCounter();

        // タイマーを開始する
        timer.StartCounter();
    }

    // フレーム毎に実行される処理
    private void Update(){

        // countTime に経過時間を取得する
        countTime = timer.GetCountTime();

        // remainTime に残り時間を代入する
        remainTime = timeLimit - countTime;

        // 残り時間が無くなったならば
        if(remainTime <= 0f){

            // ゲームが終了していないならば
            if(!gameSet){

                // TimeUpメソッドを呼び出す
                TimeUp();

                // ゲームが終了した
                gameSet = true;

            }

        }

        // スコアのテキストを更新する
        SetScoreText();

        // 残り時間のテキストを更新する
        countTimeText.text = remainTime.ToString("F0");

        // プログレスサークル（残り時間）を更新する
        remainTimeImage.fillAmount = remainTime / timeLimit;

        // ゲームが終了していないならば
        if(!gameSet){

            // マウスのボタンが下がった瞬間ならば
            if(Input.GetMouseButtonDown(0)){

                // トレースを始める
                traceObjects.TraceStart();
            
            }

            // マウスのボタンが下がっているならば
            if(Input.GetMouseButton(0)){

                // トレースしている
                traceObjects.Trace();
            
            }

            // マウスのボタンが上がった瞬間ならば
            if(Input.GetMouseButtonUp(0)){

                // トレースを終える
                traceObjects.TraceEnd();

                // 削除するボールを取得する
                List<GameObject> deleteList = traceObjects.GetTracedObjects();

                // 削除するボールが存在するならば
                if(deleteList != null){

                    // 次に生成するボールの個数を取得する
                    nextSpawnNumber = deleteList.Count;

                    // 削除するボールのそれぞれに対して
                    foreach(GameObject item in deleteList){

                        // 削除するボールの個数を３乗した値をスコアに加算する
                        score.AddScore((int)Mathf.Pow(nextSpawnNumber, 3));

                        // ボールを削除する
                        Destroy(item);
                    
                    }

                    // nextSpawnNumber（個）のボールを生成する
                    spawnController.Spawn(nextSpawnNumber);
                
                }
            }
        }

    }

    // 現在のスコアを表示
    private void SetScoreText(){
        scoreText.text = $"{score.GetScore().ToString("###,###,##0")}";
    }

    // トータルスコアを表示する
    public void TimeUp(){
        timeUpCanvas.enabled = true;
        totalScoreText.text = $"SCORE : {score.GetScore().ToString("###,###,##0")}";
    }

    // ゲームを再ロードする
    public void LoadTitle(){
        UnityEngine.SceneManagement.SceneManager.LoadScene("SampleScene");
    }
}