using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ballScript : MonoBehaviour
{
    public Rigidbody rb;  // rigidbodyを宣言(アタッチ)
    private Vector3 force = new Vector3(0.0f, 1.0f, 0.0f);// forceという名前で力を設定

    public AudioSource aus; // 自身の名前
    public AudioClip coll; // 衝突したときのSE

    int sai;
    // Start is called before the first frame update
    void Start()
    {
        // sai = Random.Range(1, 7);
        // Debug.Log("sai : " + sai);
    }

    // Update is called once per frame
    void Update()
    {
        if(Input.GetKey(KeyCode.UpArrow)){
            Debug.Log("UP");
            rb.AddForce(force);
            // transform.Translate(0f, 0.01f, 0f);
        }
        if(Input.GetKeyUp(KeyCode.Space)){
            Debug.Log("space left");
        }
    }

    void OnCollisionEnter(Collision collision){
        // if(collision.gameObject.name == "flore"){
        //     transform.Translate(0f, 5f, 0f);
        // }
        aus.clip = coll;
        aus.Play();
        Debug.Log(collision.gameObject.name);
    }
}
