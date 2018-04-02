using System;
using System.Collections.Generic;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.ServiceModel.Web;
using System.Text;

namespace CurrentVideoService
{
    // NOTE: You can use the "Rename" command on the "Refactor" menu to change the class name "Service1" in code, svc and config file together.
    // NOTE: In order to launch WCF Test Client for testing this service, please select Service1.svc or Service1.svc.cs at the Solution Explorer and start debugging.
    public class ImageService : IVideoGrabService
    {
        public Image GetImageById(int RADDeviceID)
        {
            Image result = null;
            SqlDataReader imageReader;

            SqlConnection conn = new SqlConnection(ConfigurationManager.ConnectionStrings["DefaultConnection"].ToString());
            string selectString = "[dbo].[GetImageByID]";
            SqlCommand selectCommand = new SqlCommand(selectString, conn);
            selectCommand.CommandType = CommandType.StoredProcedure;
            selectCommand.Parameters.AddWithValue("@RADDeviceID", RADDeviceID.ToString());

            conn.Open();
            imageReader = selectCommand.ExecuteReader(CommandBehavior.CloseConnection);
            while (imageReader.Read())
            {
                result = Image.FromStream(new MemoryStream((byte[])imageReader.GetValue(1)));
            }
            return result;
        }

        public void InsertImage(int RADDeviceID, string imageName, string imagePath)
        {
            System.IO.FileStream fs = new System.IO.FileStream(imagePath, System.IO.FileMode.Open);
            byte[] imageAsBytes = new byte[fs.Length];
            fs.Read(imageAsBytes, 0, imageAsBytes.Length);
            fs.Close();
            SqlConnection conn = new SqlConnection(ConfigurationManager.ConnectionStrings["DefaultConnection"].ToString());
            string insertString = "[dbo].[InsertNewImage]";

            SqlCommand insertCommand = new SqlCommand(insertString, conn);
            insertCommand.CommandType = CommandType.StoredProcedure;
            insertCommand.Parameters.AddWithValue("@RADDeviceID", RADDeviceID);
            insertCommand.Parameters.AddWithValue("@Caption", imageName);
            insertCommand.Parameters.AddWithValue("@Content", imageAsBytes);
            conn.Open();
            insertCommand.ExecuteNonQuery();
            conn.Close();
        }
    }
}
