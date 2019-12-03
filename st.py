
if(isMatEmpty(originalMat)){
        Log.i(TAG, "Empty Original Mat at testBrownPixCoutn()");
}
else{
        //Perform:
        Mat maskMat = Imgcodecs.imread(testFilePath);
        Mat bgr = new Mat();
        Imgproc.cvtColor(maskMat, bgr, Imgproc.COLOR_BGR2RGB);
        Mat maskMatHsv = new Mat();
        Imgproc.cvtColor(bgr, maskMatHsv , Imgproc.COLOR_RGB2HSV);

        //iF NOt; use RGB2HSV:
        Mat brownMat = new Mat();
        Scalar min_brown = new Scalar(20,100,100);
        Scalar max_brown = new Scalar(30,255,255);
        Core.inRange(maskMatHsv, min_brown, max_brown, brownMat);
        Log.i(TAG, "Brown Mat Non-zeros:" + Core.countNonZero(brownMat));

        Bitmap bitmapMat = Bitmap.createBitmap(brownMat.cols(), brownMat.rows(), Bitmap.Config.ARGB_8888);
        Utils.matToBitmap(brownMat, bitmapMat);
        imgView_testView.setImageBitmap(bitmapMat);

