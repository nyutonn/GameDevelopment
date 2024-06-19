using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class c : MonoBehaviour
{
    public Rigidbody rb;
    Vector3 v = new Vector3(0f, 1f, 0f);

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if(Input.GetKey(KeyCode.J)){
            if(gameObject.name == "a"){
                rb.AddForce(v, ForceMode.Force);
            }
            if(gameObject.name == "b"){
                rb.AddForce(v, ForceMode.Acceleration);
            }
            if(gameObject.name == "c"){
                rb.AddForce(v, ForceMode.Impulse);
            }
            if(gameObject.name == "d"){
                rb.AddForce(v, ForceMode.VelocityChange);
            }
        }
    }
}
