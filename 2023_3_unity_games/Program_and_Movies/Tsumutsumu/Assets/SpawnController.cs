using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// GameController に付与されるコンポーネント
public class SpawnController : MonoBehaviour
{
    // 動物のボールのprefabが４つ入るリストです
    public GameObject[] items;

    // ボールを生成する間隔（秒）
    private float spawnSpan = 0.05f;

    // ランダムな位置からランダムな角度のランダムなボールを生成する
    public void Spawn(){

        //生成するときに、xの位置を-2〜2でランダムに、Z軸で20〜-20度回転させます
        float randPosX = Random.Range(-2f, 2f);
        float randRotZ = Random.Range(-20, 20);

        // items[Random.Range(0, items.Length)]　この意味は、
        // 0~4（リストの長さ（つまり動物ボールの４個））の間のランダムな数値の順番でプレハブを取得する
        Instantiate(items[Random.Range(0, items.Length)], new Vector3(randPosX, 5f, 0f), Quaternion.Euler(new Vector3(0,0, randRotZ)));
    }

    // SpawnInOrderを呼び出す（ボール生成）
    public void Spawn(int number){
        StartCoroutine(SpawnInOrder(number));
    }

    // number（個）のボールを非同期かつspawnSpan（秒）の間隔で生成する
    private IEnumerator SpawnInOrder(int number){

        // number（回）ループを繰り返す
        for(int i = 0; i < number; i++){

            // ランダムな位置からランダムな角度のランダムなボールを一つだけ生成する
            Spawn();

            // spawnSpan（秒）だけ他に処理を譲る
            yield return new WaitForSeconds(spawnSpan);

        }
    
    }
}