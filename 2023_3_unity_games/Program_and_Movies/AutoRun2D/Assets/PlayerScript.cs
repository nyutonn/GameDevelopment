using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PlayerScript : MonoBehaviour
{
    
    public Text gameOverText;
    public Text goalText;
    bool jumpFlag = false;
    public bool gameOverFlag = false;
    public bool goalFlag = false;
    // here!!
    public int life;

    public Material[] ColorSet = new Material[4];  //  Material格納
    public Rigidbody rb;

    float speed;

    //  here!!
    // 重力を変更
    float jumpPower;
    public Vector3 localGravity;

    //  fireゲットのフラグ
    public bool fireFlag = false;
    public GameObject item;
    public GameObject item2;

    // Start is called before the first frame update
    void Start()
    {
        gameOverText.text = "";
        goalText.text = "";
        life = 3;
        // speed = 0.03f;
        // Debug.Log(life);
        // rb = GetComponent<Rigidbody>();
        
    }

    // Update is called once per frame
    void Update()
    {
        // here!
        //  ライフが削られるとスピードが遅くなり、重力が弱くなる
        if(life == 3){
            speed = 0.03f;
            jumpPower = 1000f;
            // localGravity = new Vector3(0f, -10f, 0f);
        }
        else if(life == 2){
            speed = 0.02f;
            jumpPower = 1000f * 0.75f;
            localGravity = new Vector3(0f, -10f * 0.66f * 0.66f, 0f);
        }
        else if(life == 1){
            speed = 0.01f;
            jumpPower = 1000f * 0.5f;
            localGravity = new Vector3(0f, -10f * 0.33f * 0.33f, 0f);
        }
        else if(life == 0){
            speed = 0f;
            jumpPower = 0f;
            localGravity = new Vector3(0f, -100f, 0f);
        }

        //  ジャンプ
        rb.AddForce(localGravity, ForceMode.Acceleration);  //  ローカルで重力を設定
        if(Input.GetKeyDown(KeyCode.Space) && !jumpFlag){
            rb.AddForce(transform.up * jumpPower, ForceMode.Force);
            jumpFlag = true;
        }

        //  fireボールを出す
        if(fireFlag && Input.GetKeyDown(KeyCode.Return)){
            Instantiate(item2, transform.position + new Vector3(3f, 1f, 0f), transform.rotation);
            fireFlag = false;  //  一度打ったら終了
            // Destroy(item);  //  fireCrownを消す
        }

        //  ゴールの判定
        if(gameOverFlag == false && goalFlag == false){
            transform.Translate(speed, 0f, 0f);
        }
        else if(gameOverFlag == true){
            gameOverText.text = "Game Over";
        }
        else if(goalFlag == true){
            goalText.text = "Goal!";
        }
    }

    void OnTriggerEnter(Collider other){
        //  敵とぶつかったとき
        if(other.gameObject.name == "underLine"){
            life -= 3;
        }
        //  プレハブから作ったクローンは名前が異なるので部分文字列の検索をする
        if(other.gameObject.name.Contains("upDownEnemy")){
            life -= 1;
        }
        if(other.gameObject.name.Contains("stopEnemy")){
            life -= 1;
        }
        if(other.gameObject.name.Contains("leftEnemy")){
            life -= 2;
        }
        if(other.gameObject.name.Contains("heal") && life < 3){
            life += 1;
        }

        //  fireゲット
        if(other.gameObject.name == "fire"){
            Instantiate(item, transform.position + new Vector3(0f, 0.6f, 0f), transform.rotation,
                        gameObject.transform);
            fireFlag = true;
        }

        // ゴール判定
        if(other.gameObject.name == "Goal"){
            goalFlag = true;
            Debug.Log("Goal!!");
        }

        // ゲームオーバー判定
        if(life <= 0) {
            life = 0;
            gameOverFlag = true;
            GetComponent<MeshRenderer>().material = ColorSet[0];
        }

        //  here!!
        //  Materialを変更する
        if(life == 3) GetComponent<MeshRenderer>().material = ColorSet[3];
        else if(life == 2) GetComponent<MeshRenderer>().material = ColorSet[2];
        else if(life == 1) GetComponent<MeshRenderer>().material = ColorSet[1];
        Debug.Log(life);
    }

    void OnCollisionEnter(Collision collision){
        //  地面とぶつかったときにjumpFlagを戻す
        jumpFlag = false;
    }
}
