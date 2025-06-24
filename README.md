# Max_Letters

Repo for working with the Maximo Gomez's letters. The letters are in JPEG format and need to be transcribed from image to text. For this propuse, a pretrained model (*Coloso*) from [Transkribus](https://www.transkribus.org/) will be used.

After transcription, sentimental analisys will be performed 

To run the container run:

```bash
docker-compose up -d
```
 To stop and remove container, run:

 ```bash
 docker-compose down
 ```