using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class fireCrownScript : MonoBehaviour
{
    public PlayerScript ps;
    float speed;
    // Start is called before the first frame update
    void Start()
    {
        // speed = 0.03f;
        ps = GameObject.Find("Player").GetComponent<PlayerScript>();
    }

    // Update is called once per frame
    void Update()
    {
        // speed = 0.01f * ps.life;
        // if(ps.gameOverFlag == false && ps.goalFlag == false){
        //     transform.Translate(speed, 0f, 0f);
        // }

        if(!ps.fireFlag){
            Destroy(gameObject);
        }

        // if(ps.jumpFlag){
        //     rb.AddForce(ps.localGravity, ForceMode.Acceleration);  //  ローカルで重力を設定
        // }
    }
}
