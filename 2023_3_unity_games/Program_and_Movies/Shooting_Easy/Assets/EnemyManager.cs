using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class EnemyManager : MonoBehaviour
{
    public GameObject enemy;
    public GameObject boss;
    public GameObject player;
    public Text gameText;
    // Start is called before the first frame update
    void Start()
    {
        gameText.text = "";
        for(int i = -7; i <= 7.5; i += 1){
            Instantiate(enemy, new Vector3(i, 8f, 10f), transform.rotation);
        }
    }

    // Update is called once per frame
    void Update()
    {
        if(boss == null){
            gameText.text = "Game Clear";
        }
        if(player == null){
            gameText.text = "Game Over";
        }
    }
}
