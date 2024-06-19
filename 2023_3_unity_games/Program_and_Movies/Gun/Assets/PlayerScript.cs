using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PlayerScript : MonoBehaviour
{
    public GameObject Bullet;
    public Transform Muzzle;

    int Remaining = 10;

    public Text GameText;
    public Slider slider;
    // Start is called before the first frame update
    void Start()
    {
        slider.value = 0.5f;
    }

    // Update is called once per frame
    void Update()
    {
        GameText.text = "弾数 : " + Remaining;
        if (Remaining != 0)
        {
            if (Input.GetMouseButtonDown(0))
            {
                Remaining = Remaining - 1;
                Instantiate(Bullet, Muzzle.position, Muzzle.transform.rotation);
            }
        }

    }

    private void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.name == "Bullet")
        {
            Destroy(collision.gameObject);
            Remaining = Remaining + 1;
        }
    }
}
