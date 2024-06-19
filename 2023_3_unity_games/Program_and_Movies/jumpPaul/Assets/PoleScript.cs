using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PoleScript : MonoBehaviour
{
    public float speed = 0.5f;
    public Rigidbody playerrb;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        transform.Rotate(0f, speed, 0f);
    }

    void OnCollisionEnter(Collision collision){
        if(collision.gameObject.name == "player"){
            playerrb.AddForce(transform.forward * -10f, ForceMode.Impulse);
        }
    }
}
