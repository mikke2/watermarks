import moviepy.editor as mp

video = mp.VideoFileClip("video.MOV")

logo = (mp.ImageClip("logo.png")
          .set_duration(video.duration)
          .resize(height=400) # if you need to resize...
          .margin(right=8, top=8, opacity=0) # (optional) logo-border padding
          .set_pos(("right","top")))

final = mp.CompositeVideoClip([video, logo])
final.write_videofile("test.mp4")