using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PlayerScript : MonoBehaviour
{
    float speed = 0.01f;
    int score = 0;
    bool goalFlag = false;

    public Text scoreText;
    public Text goalText;

    public AudioSource aus;
    public AudioClip coinAC;
    public AudioClip goalAC;
    // Start is called before the first frame update
    void Start()
    {
        goalText.text = "";
    }

    // Update is called once per frame
    void Update()
    {
        scoreText.text = "Score : " + score;

        if(!goalFlag){
            transform.Translate(0f, 0f, speed);
            //  left
            if(Input.GetKeyDown(KeyCode.A) && transform.position.x > -1f){
                transform.Translate(-2f, 0f, 0f);
            }
            //  right
            if(Input.GetKeyDown(KeyCode.D) && transform.position.x < 1f){
                transform.Translate(2f, 0f, 0f);
            }
        }
    }
    
    void OnCollisionEnter(Collision collision){
        if(collision.gameObject.CompareTag("Goal")){
            aus.clip = goalAC;
            aus.Play();
            goalFlag = true;
            goalText.text = "GOAL!";
            Debug.Log("Goal!");
        }
        if(collision.gameObject.CompareTag("turkey")){
            Destroy(collision.gameObject);
            speed *= 2;
            Debug.Log("お腹がふくれた");
        }
        if(collision.gameObject.CompareTag("coin")){
            aus.clip = coinAC;
            aus.Play();
            Destroy(collision.gameObject);
            score += 1;
            Debug.Log("コインゲット！");
        }
        if(collision.gameObject.CompareTag("fence")){
            Debug.Log("足をくじいた");
        }
    }
    // void OnTriggerEnter(Collider other){
    //     if(other.gameObject.CompareTag("fence")){
    //         Destroy(other.gameObject);
    //         Debug.Log("wao");
    //     }
    // }
}
