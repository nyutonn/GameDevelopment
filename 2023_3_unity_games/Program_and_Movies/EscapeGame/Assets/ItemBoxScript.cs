using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ItemBoxScript : MonoBehaviour
{
    public Text gameText;
    bool keyflag = false;
    
    public Sprite keySprite;
    public GameObject key;
    // public GameObject slot;
    public Image slotImage;
    public GameObject door;

    // Start is called before the first frame update
    void Start()
    {
        // slotImage = slot.GetComponent<Image>();
        gameText.text = "";
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void ItemClick(){
        keyflag = true;
        Destroy(key);
        Debug.Log("key Get");
        slotImage.sprite = keySprite;
    }

    public void DoorClick(){
        if(keyflag){
            Destroy(door);
            gameText.text = "OPEN";
        }
        else{
            gameText.text = "LOCKED";
        }
    }

    
}
