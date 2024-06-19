using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class SampleScript : MonoBehaviour
{
    Transform tf;
    Rigidbody rbSphere;
    public GameObject sphere;
    public Slider slider;
    // Start is called before the first frame update
    void Start()
    {
        tf = GetComponent<Transform>();
        Debug.Log(tf.position);
        rbSphere = sphere.GetComponent<Rigidbody>();
        rbSphere.AddForce(new Vector3(0f, 500f, 0f), ForceMode.Force);
        slider.value = 0.5f;
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
