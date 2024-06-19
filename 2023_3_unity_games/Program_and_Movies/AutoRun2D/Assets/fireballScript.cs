using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class fireballScript : MonoBehaviour
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
        speed = 0.01f * ps.life;
        if(ps.gameOverFlag == false && ps.goalFlag == false){
            transform.Translate(speed, 0f, 0f);
        }
    }

    void OnTriggerEnter(Collider other){
        Debug.Log("Destroy!!");

        //  here!!
        Destroy(other.gameObject);  
        Destroy(gameObject);
    }
}
