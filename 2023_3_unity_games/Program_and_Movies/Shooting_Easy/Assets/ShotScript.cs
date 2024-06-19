using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ShotScript : MonoBehaviour
{
    public float speed;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        transform.Translate(0f, speed, 0f);
        if(transform.position.y < -20 || 20 < transform.position.y){
            Destroy(gameObject);
        }
    }

    void OnCollisionEnter(Collision collision){
        Destroy(gameObject);
        Destroy(collision.gameObject);
    }
}
