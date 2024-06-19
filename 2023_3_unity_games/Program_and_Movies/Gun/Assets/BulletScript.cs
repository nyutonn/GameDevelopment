using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BulletScript : MonoBehaviour
{
    public Rigidbody rb;
    private float Power = 1000.0f;
    // Start is called before the first frame update
    void Start()
    {
        name = "Bullet";
        rb.AddForce(transform.forward * Power);
    }

    // Update is called once per frame
    void Update()
    {
        if (transform.position.y < -1)
        {
            Destroy(this.gameObject);
        }
    }
}
