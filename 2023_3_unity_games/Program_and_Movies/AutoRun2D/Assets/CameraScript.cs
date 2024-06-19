using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraScript : MonoBehaviour
{
    //  here!!
    public PlayerScript ps;
    float speed;
    void Start()
    {
        //  here!!!
        ps = GameObject.Find("Player").GetComponent<PlayerScript>();
    }

    void Update()
    {
        speed = 0.01f * ps.life;
        if(ps.gameOverFlag == false && ps.goalFlag == false){
            transform.Translate(speed, 0f, 0f);
        }
    }
}
