using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RobotScript : MonoBehaviour
{
    public Transform goaltf;
    public Transform packtf;
    public Rigidbody packrb;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        transform.LookAt(goaltf);
        float x = transform.position.x;
        float y = transform.position.y;
        transform.position = new Vector3(x, y, packtf.position.z);
    }

    void OnCollisionEnter(Collision collision){
        packrb.AddForce(transform.forward / 100, ForceMode.Impulse);
    }
}
