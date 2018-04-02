#import pypyodbc


#connection = pypyodbc.connect('Driver={SQL Server};'
#                                'Server=73.65.191.178;'
#                                'Database=Video-Up;'
#                                'uid=Video-Up;pwd=vup123')
#cursor = connection.cursor() 

#SQLCommand = ("SELECT [StreamedVideo] from [Video-Up].[dbo].[Media] where [MediaID] = ?")
#Values = [58]

#cursor.execute(SQLCommand,Values)
#results = cursor.fetchall()
#connection.close()

##Bring it back as an image
#imgBuffer2 = StringIO(results[0])
#img2 = Image.open(imgBuffer2)

##Image.show is meant for debugging and testing.
##It may generate messages about 'sleep' not being recognized
##but it works nicely for a test script like this one.
#img2.show()

import pyscreenshot as ImageGrab

if __name__ == "__main__":
    # fullscreen
    im=ImageGrab.grab()
    im.show()