using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// debug 完了！！
// OnCollisionEnter の AddForce 内に問題あり
// 座標をそのまま new Vector3 で指定してしまうと世界座標のz座標になってしまう
// transform.forward とすることで NPC (blue) 基準でz座標を見ることになる
public class NPCscript2 : MonoBehaviour
{
    Rigidbody rb;
    Transform pack_tf;
    Transform blue_tf;
    Transform tf;
    float posZ;
    public GameObject pack;
    public Rigidbody pack_rb; // 追加
    public GameObject blue;
    // public GameObject goal;
    public Transform goal_tf;
    float pack_posZ;
    float blue_posZ;
    public float speed;
    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        //transform.LookAt(goal.transform,Vector3.up);
        transform.LookAt(goal_tf, Vector3.up);
        rb = pack.GetComponent<Rigidbody>();
        pack_tf = pack.GetComponent<Transform>();
        blue_tf = blue.GetComponent<Transform>();
        pack_posZ = pack_tf.position.z;
        blue_posZ = blue_tf.position.z;
        //if (pack_posZ > blue_posZ)
        //{
        //     transform.Translate(0f, 0f, speed,Space.World);
        // }
        // if (pack_posZ < blue_posZ)
        // {
        //     transform.Translate(0f, 0f, speed*-1f,Space.World);
        // }
        tf = pack.GetComponent<Transform>();
        posZ = tf.position.z;
        transform.position = new Vector3(8f, -9f, posZ);

        // Debug.Log(rb); // デバッグ
        //Invoke("Test1", 5.0f);
    }
    void OnCollisionEnter(Collision collision)
    {
        float power = -0.01f;
        if(collision.gameObject.name == "pack")
        {
            // バグの原因はここ！
            // rb.AddForce(new Vector3(0f, 0f, power), ForceMode.Impulse); // これだと世界の座標なので力が下向きになる
            rb.AddForce(transform.forward / 100, ForceMode.Impulse); // transform.forwardでNPC基準の前になる 
        }
       
    }
   // void Test1()
   // {
   //     tf = pack.GetComponent<Transform>();
   //     posZ = tf.position.z;
   //     transform.position = new Vector3(7f, 1f, posZ);
   //     Debug.Log("aaa");
   //  }
}
